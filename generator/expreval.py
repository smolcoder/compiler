from ast import BaseASTListener
from generator.jasminprocessor import JPROC


class ExpressionListener(BaseASTListener):
    def enterBoolLiteral(self, ast):
        ast.code = JPROC.pushBool(ast.value)

