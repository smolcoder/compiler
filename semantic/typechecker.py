from ast import BaseASTListener, ASTWalker, walkAST
from env import GlobalEnv
from errors import NameNotFoundError


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


def typeCheck(ast, env):
    listener = TypeCheckListener(env)
    walkAST(listener, ast)
    return listener.errors