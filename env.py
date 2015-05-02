from ast import walkAST
from ast import BaseASTListener
from errors import NameAlreadyDefinedError
from utils import Stack


class Env:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}  # variables (name, type)
        self.build_ins = {
            'readln': {'returnType': 'None'},
            'writeln': {'returnType': 'None'},
        }

    def isBuildIn(self, name):
        return name in self.build_ins

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

    def resolveBuildIn(self, name):
        return self.build_ins.get(name)


class GlobalEnv(Env):
    def __init__(self, ast):
        Env.__init__(self, ast)
        self.functions = {}  # signatures (arguments, return type)
        self.records = {}    # record's Env

    def putFunction(self, ast):
        name = ast.getName()
        if name in self.functions or name in self.records or self.isBuildIn(name):
            return False
        self.functions[name] = {'type': ast.getReturnType(), 'args': ast.getArguments(), 'ast': ast}
        return True

    def putRecord(self, ast):
        name = ast.left.value
        if name in self.records or name in self.functions or self.isBuildIn(name):
            return False
        self.records[name] = {'env': ast.env, 'ast': ast}
        return True

    def resolveFunction(self, name):
        return self.resolveBuildIn(name) or self._resolveName(name, 'functions')

    def resolveRecord(self, name):
        return self._resolveName(name, 'records')


class BuildEnvListener(BaseASTListener):
    def __init__(self):
        self.stack = Stack()
        self.globalEnv = None
        self.errors = []

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
            self.errors.append(NameAlreadyDefinedError(ast.left.value, ast.left.source))
        self.stack.push(ast.env)

    def enterVariableDeclaration(self, ast):
        env = self.stack.top()
        if not env.putVariable(ast.getName(), ast.getType(), ast):
            self.errors.append(NameAlreadyDefinedError(ast.getName(), ast.source))

    def exitRecordBody(self, ast):
        self.stack.pop()

    def enterFunctionDeclaration(self, ast):
        ast.env = Env(ast)
        self.stack.push(ast.env)
        s = ast.getFirstChild()  # signature
        if not self.globalEnv.putFunction(s):
            self.errors.append(NameAlreadyDefinedError(s.getName(), s.source))

    def enterFunctionSignature(self, ast):
        env = self.stack.top()
        for i, (name, _type) in enumerate(ast.getArguments()):
            varAst = ast.getChild(1).getChild(i)
            if not env.putVariable(name, _type, varAst):
                self.errors.append(NameAlreadyDefinedError(name, varAst.source))

    def exitFunctionDeclaration(self, ast):
        self.stack.pop()


def buildEnv(ast):
    listener = BuildEnvListener()
    walkAST(listener, ast)
    return listener.globalEnv, listener.errors