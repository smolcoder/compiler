from distutils.errors import CompileError
from ast import BaseASTListener, walkAST
from env import GlobalEnv
from errors import NameNotFoundError, TypeMismatchError, TypeNotFoundError, CompilerError
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
        recordInfo = self.env.resolveRecord(name)
        if recordInfo:
            ast.type = name
        elif functionInfo:
            ast.type = functionInfo['ast'].getReturnType()
        else:
            raise Exception("Existence listener skipped this case!")

    def exitFunctionInvocation(self, ast):
        pass

    # def exitLiteral(self, ast):
    #     ast.type = ast.getFirstChild().type
    #
    # def exitCortegeInitializer(self, ast):
    #     ast.type = []
    #     for c in ast.getChildren():
    #         ast.type.append(c.type)

    def enterLeftHandSide(self, ast):
        env = ast.getEnv()
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            t, e = getVariableType(fc, env)
            if e:
                self.errors.append(e)
            else:
                ast.type = t
        elif fc.name == 'cortegeAccess':
            t, e = getCortegeAccessType(fc)
            if e:
                self.errors.append(e)
            else:
                ast.type = t
        else:
            t, e = getFieldAccessType(fc, self.env)
            if e:
                self.errors.append(e)
            else:
                ast.type = t

    def exitExpression(self, ast):
        chCount = len(ast.getChildren())
        fc = ast.getFirstChild()

        # if chCount == 1:
        #     ast.type = fc.type
        # elif fc.name == 'UnaryOperator':
        #     t = ast.getChild(1).type
        #     if fc.value == '!':
        #         if t != 'Bool':
        #             self.errors.append(TypeMismatchError(fc.source, msg="can't apply '!' to {}".format(t)))
        #         ast.type = 'Bool'  # assign type any way for recovery
        #     elif fc.value == '-':
        #         if t != 'Int':
        #             self.errors.append(TypeMismatchError(fc.source, msg="can't apply '-' to {}".format(t)))
        #         ast.type = 'Int'




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
    :return: (type, error)
    """
    env = env or rfa.getEnv()
    c = rfa.getFirstChild()
    if len(rfa.getChildren()) == 1:
        if c.name == 'cortegeAccess':
            return getCortegeAccessType(c, env)
        return getVariableType(c, env)
    name = c.value
    curFieldInfo = env.resolveVariable(name)
    if not curFieldInfo:
        return None, NameNotFoundError(name, c.source)
    type_ = curFieldInfo['type']
    source = curFieldInfo['ast'].source
    if isPrimitive(type_):
        return None, CompilerError('Type {} is not a record.'.format(type_), source)
    recInfo = globalEnv.resolveRecord(type_)  # todo is it needed? see RecordTypeExistenceListener
    if not recInfo:
        return None, TypeNotFoundError(type_, source)
    return getFieldAccessType(rfa.getChild(1), globalEnv, recInfo['env'])


def typeCheck(ast, env):  # todo remove env argument
    listener = TypeCheckListener(env)
    walkAST(listener, ast)
    return listener.errors


def isCortege(typeName):
    return isinstance(typeName, list)