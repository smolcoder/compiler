from distutils.errors import CompileError
from ast import BaseASTListener, ASTWalker, walkAST
from env import GlobalEnv
from errors import NameNotFoundError, TypeMismatchError


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


def getCortegeAccessType(ast):
    fc = ast.getFirstChild()
    if fc.name == 'cortegeAccess':
        outerType, error = getCortegeAccessType(fc)
        if isinstance(outerType, CompileError):
            return None, error
    else:
        name = ast.getFirstChild().value
        info = ast.getEnv().resolveVariable(name)
        if not info:
            return None, NameNotFoundError(name, ast.source)
        outerType = info['type']
    if not isCortege(outerType):
        return None, TypeMismatchError(ast.source)
    access = int(ast.getChild(1).value)
    if access >= len(outerType):
        return None, TypeMismatchError(ast.getChild(1).source, '{} - out of bound'.format(access))
    return outerType[access], None


def typeCheck(ast, env):
    listener = TypeCheckListener(env)
    walkAST(listener, ast)
    return listener.errors


def isCortege(typeName):
    return isinstance(typeName, list)