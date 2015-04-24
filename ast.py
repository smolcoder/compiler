from grammar.gen.LLangListener import LLangListener
from antlr4 import *


class ASTNode:
    def __init__(self, name, error_info=None, is_terminal=False):
        self.name = name
        self.is_terminal = is_terminal
        self.error_info = error_info
        self._children = []
        self.left = None
        self.right = None

    def addChild(self, ast):
        if self._children:
            ast.left = self._children[-1]
            self._children[-1].right = ast
        self._children.append(ast)

    def __str__(self):
        return self.name


class TerminalASTNode(ASTNode):
    def __init__(self, name, error_info=None):
        ASTNode.__init__(self, name, error_info, True)

    def addChild(self, ast):
        raise Exception("You can not add child to terminal vertex.")


class ErrorASTNode(TerminalASTNode):
    def __init__(self, error_info):
        TerminalASTNode.__init__(self, 'Error', error_info)


SKIP_SYMBOLS = ['[', ']', '{', '}', '(', ')', ';', ',', '.']


def get_rule_name(ctx):
    return ctx.parser.ruleNames[ctx.getRuleIndex()]


# Builds AST node for each state context,
# binds it to the context (via making ast field)
class ASTBuildListener(LLangListener):
    def enterEveryRule(self, ctx):
        node = ASTNode(get_rule_name(ctx))
        ctx.ast = node
        if ctx.parentCtx:
            ctx.parentCtx.ast.addChild(node)

    def visitTerminal(self, node):
        text = node.symbol.text
        if text in SKIP_SYMBOLS:
            return
        if node.parentCtx.ast.name == 'strLiteral':
            text = text[1:len(text) - 1]
        ast = TerminalASTNode(text)
        node.parentCtx.ast.addChild(ast)

    def visitErrorNode(self, node):
        symbol = node.symbol
        text = symbol.source[1].strdata
        start = symbol.start
        stop = symbol.stop
        while start - 1 >= 0 and text[start - 1] != '\n':
            start -= 1
        while stop + 1 < len(text) and text[stop + 1] != '\n':
            stop += 1

        ast = ErrorASTNode((text[start:stop + 1], symbol.line, symbol.column))
        node.parentCtx.ast.addChild(ast)


def buildAST(root):
    listener = ASTBuildListener()
    walker = ParseTreeWalker()
    walker.walk(listener, root)
    return root.ast