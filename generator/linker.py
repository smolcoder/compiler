from ast import NonTerminalASTNode, walkAST
from middlecode import BuildMiddleCodeListener


class MiddleCodeLinker:
    def __init__(self):
        self.code = []

    def getCodeBefore(self, ast):
        if hasattr(ast, 'code_before'):
            self.code += ast.code_before

    def getCodeAfter(self, ast):
        if hasattr(ast, 'code_after'):
            self.code += ast.code_after

    def getCode(self, ast):
        if hasattr(ast, 'code'):
            self.code += ast.code

    def linkChildren(self, ast):
        if isinstance(ast, NonTerminalASTNode):
            for c in ast.getChildren():
                self.link(c)

    def linkForStatement(self, ast):
        forInit = ast.getFirstChildByName('forInit')
        forCondition = ast.getFirstChildByName('forCondition')
        forUpdate = ast.getFirstChildByName('forUpdate')
        forBlock = ast.getLastChild()
        self.link(forInit)
        self.link(forCondition)
        self.link(forBlock)
        self.link(forUpdate)

    def link(self, ast):
        self.getCodeBefore(ast)
        if ast.name == 'forStatement':
            self.linkForStatement(ast)
        else:
            self.linkChildren(ast)
            self.getCode(ast)
        self.getCodeAfter(ast)


def linkCode(ast):
    linker = MiddleCodeLinker()
    linker.link(ast)
    return linker.code


def makeTAD(ast):
    l = BuildMiddleCodeListener(ast.getGlobalEnv())
    walkAST(l, ast)
    return linkCode(ast)