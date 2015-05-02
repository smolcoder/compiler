from distutils.errors import CompileError
from ast import BaseASTListener, walkAST
from env import GlobalEnv
from errors import NameNotFoundError, TypeMismatchError, TypeNotFoundError, CompilerError
from utils import isPrimitive


class RecordTypeExistenceListener(BaseASTListener):
    def __init__(self, globalEnv):
        """
        :type globalEnv: GlobalEnv
        """
        self.errors = []
        self.env = globalEnv

    def enterExprType(self, ast):
        if ast.getFirstChild().name != 'RecordID':
            return
        name = ast.getFirstChild().typeName
        if not self.env.resolveRecord(name):
            self.errors.append(NameNotFoundError(name, ast.source))


def checkAllRecordTypesExist(ast):
    listener = RecordTypeExistenceListener(ast.env)
    walkAST(listener, ast)
    return listener.errors


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
        if not functionInfo:
            self.errors.append(NameNotFoundError(name, ast.source))
        ast.type = functionInfo['ast'].getReturnType()

    def enterLeftHandSide(self, ast):
        env = ast.getEnv()
        fc = ast.getFirstChild()
        if fc.name == 'Identifier':
            name = fc.value
            idInfo = env.resolveVariable(name)
            if not idInfo:
                self.errors.append(NameNotFoundError(name, fc.source))
            ast.type = idInfo['type']
            return
        if fc.name == 'cortegeAccess':
            name = fc.getFirstChild().name


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
        name = ca.getFirstChild().value
        env = env or ca.getEnv()
        info = env.resolveVariable(name)
        if not info:
            return None, NameNotFoundError(name, ca.source)
        outerType = info['type']
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
        # c is Identifier
        name = c.value
        idInfo = env.resolveVariable(name)
        if not idInfo:
            return None, NameNotFoundError(name, c.source)
        return idInfo['type'], None
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


def typeCheck(ast, env):
    listener = TypeCheckListener(env)
    walkAST(listener, ast)
    return listener.errors


def isCortege(typeName):
    return isinstance(typeName, list)