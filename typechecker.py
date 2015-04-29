from ast import BaseASTListener, ASTWalker


class TypeCheckListener(BaseASTListener):
    def __init__(self, globalEnv):
        self.errors = []
        self.env = globalEnv


def typeCheck(ast, env):
    listener = TypeCheckListener(env)
    walker = ASTWalker()
    walker.walk(listener, ast)
    return listener.errors