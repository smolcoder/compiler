from ast import ASTWalker
from ast import BaseASTListener
from errors import CompilerError
from utils import Stack


class Env:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}  # variables (name, type)

    def putVariable(self, name, _type, ast):
        if name in self.variables:
            return False
        self.variables[name] = {'type': _type, 'ast': ast}
        return True

    def _resolveName(self, name, whereStr):
        env = self
        while env is not None:
            where = getattr(env, whereStr)
            if where is None:
                raise Exception('Unknown field "{}" of {}'.format(whereStr, env))
            if name in where:
                return where[name]
            env = env.ast.getHigherEnv()
        return None

    def resolveVariable(self, name):
        return self._resolveName(name, 'variables')


class GlobalEnv(Env):
    def __init__(self, ast):
        Env.__init__(self, ast)
        self.functions = {}  # signatures (name, arguments, return type)
        self.records = {}    # record's Env

    def putFunction(self, ast):
        name = ast.getName()
        if name in self.functions or name in self.records:
            return False
        self.functions[name] = {'type': ast.getReturnType(), 'args': ast.getArguments(), 'ast': ast}
        return True

    def putRecord(self, ast):
        name = ast.left.value
        if name in self.records or name in self.functions:
            return False
        self.records[name] = {'env': ast.env, 'ast': ast}
        return True

    def resolveFunction(self, name):
        return self._resolveName(name, 'functions')

    def resolveRecord(self, name):
        return self._resolveName(name, 'records')


class BuildEnvListener(BaseASTListener):
    def __init__(self):
        self.stack = Stack()
        self.globalEnv = None
        self.errors = []

    def addError(self, msg, sourceInfo):
        self.errors.append(CompilerError(msg, sourceInfo.line, sourceInfo.column))

    def enterProgramme(self, ast):
        ast.env = GlobalEnv(ast)
        self.globalEnv = ast.env
        self.stack.push(ast.env)

    def enterJustBlock(self, ast):
        ast.env = Env(ast)
        self.stack.push(ast.env)

    def exitJustBlock(self, ast):
        self.stack.pop()

    def enterWhileStatement(self, ast):
        ast.env = Env(ast)
        self.stack.push(ast.env)

    def exitWhileStatement(self, ast):
        self.stack.pop()

    def enterForStatement(self, ast):
        ast.env = Env(ast)
        self.stack.push(ast.env)

    def exitForStatement(self, ast):
        self.stack.pop()

    def enterRecordBody(self, ast):
        ast.env = Env(ast)
        if not self.globalEnv.putRecord(ast):
            self.addError("Name '{}' already defined.".format(ast.left.value), ast.left.source)
        self.stack.push(ast.env)

    def enterVariableDeclaration(self, ast):
        env = self.stack.top()
        if not env.putVariable(ast.getName(), ast.getType(), ast):
            self.addError("Name '{}' already defined.".format(ast.getName()), ast.source)

    def exitRecordBody(self, ast):
        self.stack.pop()

    def enterFunctionDeclaration(self, ast):
        ast.env = Env(ast)
        self.stack.push(ast.env)
        s = ast.getFirstChild()  # signature
        if not self.globalEnv.putFunction(s):
            self.addError("Name '{}' already defined.".format(s.getName()), s.source)

    def enterFunctionSignature(self, ast):
        env = self.stack.top()
        for i, (name, _type) in enumerate(ast.getArguments()):
            env.putVariable(name, _type, ast.getChild(i))

    def exitFunctionDeclaration(self, ast):
        self.stack.pop()


def buildEnv(ast):
    walker = ASTWalker()
    listener = BuildEnvListener()
    walker.walk(listener, ast)
    return listener.globalEnv, listener.errors