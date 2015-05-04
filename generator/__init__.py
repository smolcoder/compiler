from ast import BaseASTListener, walkAST


class CodeLinkerListener(BaseASTListener):
    def __init__(self):
        self.code = []

    def exitEvery(self, ast):
        self.code += getattr(ast, 'code', [])


def linkCode(ast):
    l = CodeLinkerListener()
    walkAST(l, ast)
    return l.code


class ExpressionTADListener(BaseASTListener):
    def enterIntLiteral(self, ast):
        pass

    def exitLeftHandSide(self, ast):
        fc = ast.getFirstChild()


def recordAccessCode(ast):
    fc = ast.getFirstChild()
    if fc.name == 'Identifier':
        ast.code = ['access {} {}'.format(fc.value, ast.type)]
        return fc.value
    sc = ast.getLastChild()
    field = recordAccessCode(fc) + '.' + sc.value
    ast.code = ['access {} {}'.format(field, ast.type)]
    return field
