from ast import BaseASTListener, IntLiteralASTNode, BoolLiteralASTNode, StrLiteralASTNode, walkAST, \
    NonTerminalASTNode


TYPE_TO_AST = {
    'Int': IntLiteralASTNode,
    'Bool': BoolLiteralASTNode,
    'Str': StrLiteralASTNode
}


class ConstantPreCalculationListener(BaseASTListener):
    def exitExpression(self, ast):
        op = ast.getOperator()
        newLiteral = None

        if not op:
            return
        if ast.isUnaryOperation():
            arg = ast.getLastChild()
            if arg.isLiteral():
                newLiteral = TYPE_TO_AST[ast.type](ast.source, op.perform(arg.getDeepest().value))
        else:
            left = ast.getFirstChild()
            right = ast.getLastChild()
            if left.isLiteral() and right.isLiteral():
                newLiteral = TYPE_TO_AST[ast.type](ast.source, op.perform(left.getDeepest().value,
                                                                          right.getDeepest().value))
        if newLiteral:
            literal = NonTerminalASTNode('literal', ast.source)
            literal.addChild(newLiteral)
            ast.removeChildren()
            ast.addChild(literal)


def precalculateConstants(ast):
    l = ConstantPreCalculationListener()
    walkAST(l, ast)