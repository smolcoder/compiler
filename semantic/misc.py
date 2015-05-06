from ast import BaseASTListener, walkAST


class NormalizeRecordInitializerListener(BaseASTListener):
    def __init__(self, globalEnv):
        self.globalEnv = globalEnv

    def exitRecordFieldInitializerList(self, ast):
        varInits = {}
        recordName = ast.parent.getFirstChild().value
        env = self.globalEnv.resolveRecord(recordName)['env']
        for fieldInit in ast.getChildren():
            varInits[fieldInit.getFirstChild().value] = fieldInit
        ast.removeChildren()
        for name in env.varOrder:
            ast.addChild(varInits[name])


def normalizeRecordInitializer(ast):
    l = NormalizeRecordInitializerListener(ast.getGlobalEnv())
    walkAST(l, ast)