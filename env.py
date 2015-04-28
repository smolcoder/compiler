from ast import ASTWalker
from ast import BaseASTListener
from errors import CompilerError
from utils import Stack


class Env:
    def __init__(self):
        self.variables = {}  # variables (name, type)

    def putVariable(self, name, _type):
        if name in self.variables:
            return False
        self.variables[name] = {'type': _type}
        return True


class GlobalEnv(Env):
    def __init__(self):
        Env.__init__(self)
        self.functions = {}  # signatures (name, arguments, return type)
        self.records = {}    # record's Env

    def putFunction(self, name, arguments, returnType):
        if name in self.functions:
            return False
        self.functions[name] = {'type': returnType, 'args': arguments}
        return True

    def putRecord(self, name, env):
        if name in self.records:
            return False
        self.records[name] = env
        return True


class BuildEnvListener(BaseASTListener):
    def __init__(self):
        self.stack = Stack()
        self.globalEnv = GlobalEnv()
        self.errors = []

    def addError(self, msg, sourceInfo):
        self.errors.append(CompilerError(msg, sourceInfo.line, sourceInfo.column))

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
        if not self.globalEnv.putRecord(ast.left.value, ast.env):
            self.addError("Record '{}' already defined.".format(ast.left.value), ast.left.source)
        self.stack.push(ast.env)

    def enterVariableDeclaration(self, ast):
        env = self.stack.top()
        if not env.putVariable(ast.getName(), ast.getType()):
            self.addError("Variable '{}' already defined.".format(ast.getName()), ast.source)

    def exitRecordBody(self, ast):
        self.stack.pop()

    def enterFunctionBody(self, ast):
        ast.env = Env()
        self.stack.push(ast.env)

    def enterFunctionDeclaration(self, ast):
        ast.env = Env()
        self.stack.push(ast.env)
        s = ast.getFirstChild()  # signature
        if not self.globalEnv.putFunction(s.getName(), s.getArguments(), s.getReturnType()):
            self.addError("Function '{}' already defined.".format(s.getName()), s.source)

    def enterFunctionSignature(self, ast):
        env = self.stack.top()
        for name, _type in ast.getArguments():
            env.putVariable(name, _type)

    def exitFunctionBody(self, ast):
        self.stack.pop()


def buildEnv(ast):
    walker = ASTWalker()
    listener = BuildEnvListener()
    walker.walk(listener, ast)
    return listener.globalEnv, listener.errors