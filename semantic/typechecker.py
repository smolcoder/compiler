from distutils.errors import CompileError
from ast import BaseASTListener, walkAST, OperatorASTNode, ExpressionASTNode
from env import GlobalEnv
from errors import NameNotFoundError, TypeMismatchError, TypeNotFoundError, CompilerError, NameAlreadyDefinedError
from utils import isPrimitive


class TypeCheckListener(BaseASTListener):
    def __init__(self, globalEnv):
        """
        :type globalEnv: GlobalEnv
        """
        self.errors = []
        self.env = globalEnv

    def enterFunctionInvocation(self, ast):
        name = ast.getFirstChild().value
        functionInfo = self.env.resolveFunction(name)
        if functionInfo:
            ast.type = functionInfo['ast'].getFirstChild().getReturnType()
        else:
            raise Exception("Existence listener skipped this case!")

    def enterRecordInitializer(self, ast):
        name = ast.getFirstChild().value
        recordInfo = self.env.resolveRecord(name)
        if recordInfo:
            ast.type = name
        else:
            raise Exception("Existence listener skipped this case!")

    def exitFunctionInvocation(self, ast):
        expectedArgTypes = self.env.resolveFunction(ast.getFirstChild().value)['args']
        actualArguments = ast.getLastChild().getChildren()
        if len(actualArguments) > len(expectedArgTypes):
            self.errors.append(TypeMismatchError(ast.getLastChild().source, msg='extra arguments'))
        elif len(actualArguments) < len(expectedArgTypes):
            self.errors.append(TypeMismatchError(ast.getLastChild().source, msg='insufficient arguments'))
        else:
            for (name, exp), act in zip(expectedArgTypes, actualArguments):
                if act.type != exp:
                    self.errors.append(
                        TypeMismatchError(act.source, msg='for argument {}: {} != {}'.format(name, exp, act.type)))
                    break

    def exitRecordInitializer(self, ast):
        recordInfo = self.env.resolveRecord(ast.getFirstChild().value)
        variables = recordInfo['env'].variables
        children = ast.getLastChild().getChildren() if len(ast.getChildren()) > 1 else []
        specified = []
        if len(children) > len(variables):
            self.errors.append(TypeMismatchError(ast.getLastChild().source, msg='extra arguments'))
            return
        if len(children) < len(variables):
            self.errors.append(TypeMismatchError(ast.getLastChild().source, msg='insufficient arguments'))
            return
        for init in children:
            name = init.getFirstChild().value
            if name in specified:
                self.errors.append(NameAlreadyDefinedError(name, init.source))
                return
            specified.append(specified)
            varType = init.getLastChild().type
            if name not in variables:
                self.errors.append(NameNotFoundError(name, init.source))
                continue
            if varType != variables[name]['type']:
                self.errors.append(
                    TypeMismatchError(init.source, msg="{}: {} != {}".format(name, varType, variables[name]['type'])))

    def exitLiteral(self, ast):
        ast.type = ast.getFirstChild().type

    def exitCortegeInitializer(self, ast):
        ast.type = ast.getFirstChild().type

    def exitReadIntCall(self, ast):
        ast.type = 'Int'

    def exitReadStrCall(self, ast):
        ast.type = 'Str'

    def exitReadBoolCall(self, ast):
        ast.type = 'Bool'

    def exitExpressionList(self, ast):
        ast.type = []
        for c in ast.getChildren():
            if c.type == 'None':
                self.errors.append(TypeMismatchError(c.source))
            ast.type.append(c.type)

    def exitCortegeInitializerList(self, ast):
        ast.type = ast.getFirstChild().type

    def enterLeftHandSide(self, ast):
        env = ast.getEnv()
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            t, e = getVariableType(fc, env)
        elif fc.name == 'cortegeAccess':
            t, e = getCortegeAccessType(fc)
        else:
            t, _, e = getFieldAccessType(fc, self.env)
        if e:
            self.errors.append(e)
        ast.type = t

    def exitVariableDeclaration(self, ast):
        if not isinstance(ast.getLastChild(), ExpressionASTNode):
            return
        l_type = ast.getFirstChild().typeName
        r_type = ast.getLastChild().type
        if l_type != r_type:
            self.errors.append(TypeMismatchError(ast.getLastChild().source, msg='{} != {}'.format(l_type, r_type)))

    def exitAssignment(self, ast):
        l = ast.getFirstChild()
        op = ast.getChild(1)
        r = ast.getLastChild()
        if op.value == '=':
            if l.type != r.type:
                self.errors.append(TypeMismatchError(op.source))
        else:
            if l.type != r.type or l.type != 'Int':
                self.errors.append(TypeMismatchError(op.source))

    def exitExpression(self, ast):
        chCount = len(ast.getChildren())
        op = ast.getOperator()

        if chCount == 1:
            ast.type = ast.getFirstChild().type
            if ast.type == 'None' and ast.parent.name == 'argumentList':
                self.errors.append(TypeMismatchError(ast.source, msg='argument list can not take None type'))
            return
        if op.name == 'UnaryOperator':
            t = ast.getChild(1).type
            if op.value == '!':
                if t != 'Bool':
                    self.errors.append(TypeMismatchError(op.source, msg="can't apply '!' to {}".format(t)))
                ast.type = 'Bool'  # assign type any way for recovery
            elif op.value == '-':
                if t != 'Int':
                    self.errors.append(TypeMismatchError(op.source, msg="can't apply '-' to {}".format(t)))
                ast.type = 'Int'
            return
        l = ast.getFirstChild()
        r = ast.getLastChild()
        if isinstance(op, OperatorASTNode):
            if op.name == 'BoolOperator':
                if l.type != 'Bool' or r.type != 'Bool':
                    self.errors.append(TypeMismatchError(op.source, msg='Bool is required'))
                ast.type = 'Bool'
            elif op.name == 'EqualOrNotOperator':
                if l.type != r.type:
                    self.errors.append(TypeMismatchError(op.source, msg='{} != {}'.format(l.type, r.type)))
                ast.type = 'Bool'
            elif op.name == 'CompareOperator':
                if l.type != 'Int' or r.type != 'Int':
                    self.errors.append(TypeMismatchError(op.source, msg='Int is required'))
                ast.type = 'Bool'
            else:
                if l.type != 'Int' or r.type != 'Int':
                    self.errors.append(TypeMismatchError(op.source, msg='Int is required'))
                ast.type = 'Int'

    def exitIf(self, ast):
        t = ast.getCondition().type
        if t != 'Bool':
            self.errors.append(TypeMismatchError(ast.getCondition(), msg='Bool != {}'.format(t)))

    def exitElif(self, ast):
        t = ast.getCondition().type
        if t != 'Bool':
            self.errors.append(TypeMismatchError(ast.getCondition(), msg='Bool != {}'.format(t)))

    def exitForCondition(self, ast):
        ast.type = ast.getFirstChild().type
        if ast.type != 'Bool':
            self.errors.append(TypeMismatchError(ast.source, msg='Bool != {}'.format(ast.type)))


def getVariableType(va, env=None):
    env = env or va.getEnv()
    name = va.value
    info = env.resolveVariable(name)
    if not info:
        return None, NameNotFoundError(name, va.source)
    return info['type'], None


def getCortegeAccessType(ca, env=None):
    """
    :param ca: cortege access ast
    :return: (type, error)
    """
    fc = ca.getFirstChild()
    if fc.name == 'cortegeAccess':
        outerType, error = getCortegeAccessType(fc, env)
        if isinstance(outerType, CompileError):
            return None, error
    else:
        t, e = getVariableType(fc, env or ca.getEnv())
        if e:
            return None, e
        outerType = t
    if not isCortege(outerType):
        return None, TypeMismatchError(ca.source)
    access = int(ca.getChild(1).value)
    if access >= len(outerType):
        return None, TypeMismatchError(ca.getChild(1).source, '{} - out of bound'.format(access))
    return outerType[access], None


def getFieldAccessType(rfa, globalEnv, env=None):
    """
    :param rfa: record field access ast
    :return: (type, newEnv, error)
    """
    env = env or rfa.getEnv()
    left = rfa.getFirstChild()
    if len(rfa.getChildren()) == 1:
        t, e = getVariableType(left, env)
        if e:
            return None, None, e
        rfa.type = t
        return t, globalEnv.resolveRecord(t)['env'], e
    t, env, e = getFieldAccessType(left, globalEnv, env)
    if e:
        return None, None, e
    right = rfa.getChild(1)
    if not env:
        return None, None, CompilerError('Type {} is not a record.'.format(left.type), right.source)
    if right.name == 'cortegeAccess':
        t, e = getCortegeAccessType(right, env)
        if e:
            return None, None, e
        rfa.type = t
        return t, env, e
    t, e = getVariableType(right, env)
    if e:
        return None, None, e
    rfa.type = t
    if t in globalEnv.records:
        return t, globalEnv.resolveRecord(t)['env'], e
    return t, None, e


def typeCheck(ast, env):  # todo remove env argument
    listener = TypeCheckListener(env)
    walkAST(listener, ast)
    return listener.errors


def isCortege(typeName):
    return isinstance(typeName, list)