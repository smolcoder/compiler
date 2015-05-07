from ast import NonTerminalASTNode, walkAST
from middlecode import BuildMiddleCodeListener


class MiddleCodeLinker:
    def __init__(self):
        self.code = []

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
        self.code += ast.getCodeBefore()
        if ast.name == 'forStatement':
            self.linkForStatement(ast)
        else:
            self.linkChildren(ast)
            self.code += ast.getCode()
        self.code += ast.getCodeAfter()


def linkCode(ast):
    linker = MiddleCodeLinker()
    linker.link(ast)
    return linker.code


def makeTAC(ast):
    l = BuildMiddleCodeListener(ast.getGlobalEnv())
    walkAST(l, ast)
    return linkCode(ast)