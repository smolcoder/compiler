from ast import ASTWalker
from utils import Stack


class Env:
    def __init__(self):
        self.variables = {}


class GlobalEnv:
    def __init__(self):
        self.variables = {}  # variables (name, type)
        self.functions = {}  # signatures (name, arguments, return type)
        self.records = {}    # record's Env


class BuildEnvListener:
    def __init__(self):
        self.stack = Stack()
        self.globalEnv = GlobalEnv()

    def enterProgramme(self, ast):
        ast.env = self.globalEnv
        self.stack.push(ast.env)

    def enterJustBlock(self, ast):
        ast.env = Env()
        self.stack.push(ast.env)

    def exitJustBlock(self, ast):
        self.stack.pop()

    def enterWhileStatement(self, ast):
        ast.env = Env()
        self.stack.push(ast.env)

    def exitWhileStatement(self, ast):
        self.stack.pop()

    def enterForStatement(self, ast):
        ast.env = Env()
        self.stack.push(ast.env)

    def exitForStatement(self, ast):
        self.stack.pop()

    def enterRecordBody(self, ast):
        ast.env = Env()
        self.globalEnv.records[ast.left.value] = ast.env
        self.stack.push(ast.env)

    def enterVariableDeclaration(self, ast):
        env = self.stack.top()
        env.variables[ast.getName()] = ast.getType()

    def exitRecordBody(self, ast):
        self.stack.pop()

    def enterFunctionBody(self, ast):
        ast.env = Env()
        self.stack.push(ast.env)

    def enterFunctionDeclaration(self, ast):
        ast.env = Env()
        self.stack.push(ast.env)
        signature = ast.getFirstChild()
        self.globalEnv.functions[signature.getName()] = {
            'type': signature.getReturnType(),
            'args': signature.getArguments()
        }

    def enterFunctionSignature(self, ast):
        env = self.stack.top()
        for name, _type in ast.getArguments():
            env.variables[name] = {'type': _type}

    def exitFunctionBody(self, ast):
        self.stack.pop()


def buildEnv(ast):
    walker = ASTWalker()
    walker.walk(BuildEnvListener(), ast)
    return ast