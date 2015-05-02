from ast import BaseASTListener, walkAST
from errors import NameNotFoundError


class ExistenceCheckListener(BaseASTListener):
    """
    For records and functions only
    """
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

    def enterFunctionInvocation(self, ast):
        name = ast.getFirstChild().value
        functionInfo = self.env.resolveFunction(name)
        if not functionInfo:
            self.errors.append(NameNotFoundError(name, ast.source))

    def enterRecordInitializer(self, ast):
        name = ast.getFirstChild().value
        recordInfo = self.env.resolveRecord(name)
        if not recordInfo:
            self.errors.append(NameNotFoundError(name, ast.source))


def checkExistence(ast):
    listener = ExistenceCheckListener(ast.env)
    walkAST(listener, ast)
    return listener.errors