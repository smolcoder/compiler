from ast import walkAST
from ast import BaseASTListener
from errors import NameAlreadyDefinedError
from localvartable import LocalVariableTable
from utils import Stack


class Env:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}  # variables (name, type)
        self.varOrder = []
        self.build_ins = {
            'readInt': {'returnType': 'Int'},
            'readStr': {'returnType': 'Str'},
            'readBool': {'returnType': 'Bool'},
            'writeln': {'returnType': 'None'},
        }

    def isBuildIn(self, name):
        return name in self.build_ins

    def putVariable(self, name, _type, ast):
        if name in self.variables:
            return False
        self.variables[name] = {'type': _type, 'ast': ast, 'name': name}
        self.varOrder.append(name)
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

    def generateLocalVariableTable(self, startFrom=0):
        lvt = LocalVariableTable(startFrom)
        for v in self.varOrder:
            lvt.put(v, _type=self.variables[v]['type'], ast=self.variables[v]['ast'])
        return lvt


class GlobalEnv(Env):
    def __init__(self, ast):
        Env.__init__(self, ast)
        self.functions = {}  # signatures (arguments, return type)
        self.records = {}    # record's Env

    def putFunction(self, ast):
        name = ast.getName()
        if name in self.functions or name in self.records or self.isBuildIn(name):
            return False
        self.functions[name] = {'type': ast.getReturnType(), 'args': ast.getArguments(), 'ast': ast.parent}
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
        self.scopes = []

    def resolve(self, name):
        for s in self.scopes:
            if name in s:
                return True
        return False

    def enterProgramme(self, ast):
        ast.env = GlobalEnv(ast)
        self.globalEnv = ast.env
        self.stack.push(ast.env)

    def exitProgramme(self, ast):
        self.stack.pop()

    def enterJustBlock(self, ast):
        ast.env = Env(ast)
        self.stack.push(ast.env)
        self.scopes = [{}] + self.scopes

    def exitJustBlock(self, ast):
        self.stack.pop()
        self.scopes = self.scopes[1:]

    def enterRecordBody(self, ast):
        ast.env = Env(ast)
        self.stack.push(ast.env)
        if not self.globalEnv.putRecord(ast):
            self.errors.append(NameAlreadyDefinedError(ast.left.value, ast.left.source))

    def enterVariableDeclaration(self, ast):
        env = self.stack.top()
        if not env.putVariable(ast.getName(), ast.getType(), ast) or self.resolve(ast.getName()):
            self.errors.append(NameAlreadyDefinedError(ast.getName(), ast.source))
        else:
            if self.scopes:
                self.scopes[0][ast.getName()] = 1

    def exitRecordBody(self, ast):
        self.stack.pop()

    def enterWhileStatement(self, ast):
        ast.env = Env(ast)
        self.stack.push(ast.env)
        self.scopes = [{}] + self.scopes

    def exitWhileStatement(self, ast):
        self.stack.pop()
        self.scopes = self.scopes[1:]

    def enterForStatement(self, ast):
        ast.env = Env(ast)
        self.stack.push(ast.env)
        self.scopes = [{}] + self.scopes

    def exitForStatement(self, ast):
        self.stack.pop()
        self.scopes = self.scopes[1:]

    def enterFunctionDeclaration(self, ast):
        ast.env = Env(ast)
        self.stack.push(ast.env)
        self.scopes = [{}] + self.scopes
        s = ast.getFirstChild()  # signature
        if not self.globalEnv.putFunction(s):
            self.errors.append(NameAlreadyDefinedError(s.getName(), s.source))

    def exitFunctionDeclaration(self, ast):
        self.stack.pop()
        self.scopes = self.scopes[1:]

    def enterFunctionSignature(self, ast):
        env = self.stack.top()
        for i, (name, _type) in enumerate(ast.getArguments()):
            varAst = ast.getChild(1).getChild(i)
            if not env.putVariable(name, _type, varAst):
                self.errors.append(NameAlreadyDefinedError(name, varAst.source))


def buildEnv(ast):
    listener = BuildEnvListener()
    walkAST(listener, ast)
    return listener.globalEnv, listener.errors


def createVariableTables(ast):
    block = ast.getJustBlock()
    ast.lvt = ast.env.generateLocalVariableTable()
    if block:
        block.lvt = block.getEnv().generateLocalVariableTable(1)
        block.lvt.put('__internal__args', '[Ljava/lang/String;', number=0)
        populateLVT(block.lvt, block)
    for name in ast.env.functions:
        a = ast.env.resolveFunction(name)['ast']
        a.lvt = a.env.generateLocalVariableTable()
        populateLVT(a.lvt, a)


class PopulateLVTListener(BaseASTListener):
    def __init__(self, lvt):
        """
        :type lvt: LocalVariableTable
        """
        self.lvt = lvt

    def enterVariableDeclaration(self, ast):
        info = ast.getEnv().resolveVariable(ast.getChild(1).value)
        self.lvt.put(info['name'], info['type'], info['ast'])


def populateLVT(lvt, ast):
    l = PopulateLVTListener(lvt)
    walkAST(l, ast)