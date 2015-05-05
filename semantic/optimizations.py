from ast import BaseASTListener, IntLiteralASTNode, BoolLiteralASTNode, StrLiteralASTNode, walkAST, \
    NonTerminalASTNode


TYPE_TO_AST = {
    'Int': IntLiteralASTNode,
    'Bool': BoolLiteralASTNode,
    'Str': StrLiteralASTNode
}


class ConstantPreCalculationListener(BaseASTListener):
    errors = []

    def exitExpression(self, ast):
        if self.errors:
            return
        op = ast.getOperator()
        newLiteral = None

        if not op:
            return
        if ast.isUnaryOperation():
            arg = ast.getLastChild()
            if arg.isLiteral():
                newLiteral = TYPE_TO_AST[ast.type](ast.source, op.perform(arg.getDeepest().value,
                                                                          errors=self.errors))
        else:
            left = ast.getFirstChild()
            right = ast.getLastChild()
            if left.isLiteral() and right.isLiteral():
                newLiteral = TYPE_TO_AST[ast.type](ast.source, op.perform(left.getDeepest().value,
                                                                          right.getDeepest().value,
                                                                          errors=self.errors))
        if newLiteral:
            literal = NonTerminalASTNode('literal', ast.source)
            literal.addChild(newLiteral)
            ast.removeChildren()
            ast.addChild(literal)


def precalculateConstants(ast):
    l = ConstantPreCalculationListener()
    walkAST(l, ast)
    return l.errors