from grammar.gen.LLangListener import LLangListener
from antlr4 import *


class TypedASTNode:
    _type = None

    def getType(self):
        return self._type


class ASTNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return self.name


class TerminalASTNode(ASTNode):
    def __init__(self, name, value=None):
        ASTNode.__init__(self, name)
        self.value = value

    def __str__(self):
        return '{}[{}]'.format(self.name, self.value) if self.value is not None else self.name


class NonTerminalASTNode(ASTNode):
    def __init__(self, name):
        ASTNode.__init__(self, name)
        self._children = []

    def addChild(self, ast):
        ast.parent = self
        if self._children:
            ast.left = self._children[-1]
            self._children[-1].right = ast
        self._children.append(ast)

    def getFirstChild(self):
        return self._children[0]

    def getChild(self, index):
        return self._children[index]

    def getDeepestTerminal(self):
        if len(self._children) != 1:
            raise Exception('Node {} has two or more children.'.format(self))
        first = self.getFirstChild()
        return first if isinstance(first, TerminalASTNode) else first.getDeepestTerminal()


class ErrorASTNode(TerminalASTNode):
    def __init__(self, errorInfo):
        TerminalASTNode.__init__(self, 'Error')
        self.errorInfo = errorInfo


class StringASTNode(TerminalASTNode, TypedASTNode):
    _type = 'string'

    def __init__(self, string):
        TerminalASTNode.__init__(self, 'String')
        self.value = string


class IntASTNode(TerminalASTNode, TypedASTNode):
    _type = 'integer'

    def __init__(self, value):
        TerminalASTNode.__init__(self, 'Integer')
        self.value = value


class BoolASTNode(TerminalASTNode, TypedASTNode):
    _type = 'boolean'

    def __init__(self, value):
        TerminalASTNode.__init__(self, 'Boolean')
        self.value = value

# class UnaryOperation(NonTerminalASTNode):
#     def __init__(self, name, operator, subject):
#         NonTerminalASTNode.__init__(self, name)
#         self.operator = operator
#         self.operand = subject


SKIP_SYMBOLS = ['[', ']', '{', '}', '(', ')', ';', ',', '.', ':',
                'fun', 'return', 'readln', 'writeln', '=']


def get_rule_name(ctx):
    return ctx.parser.ruleNames[ctx.getRuleIndex()]


# Builds AST node for each state context,
# binds it to the context (via making ast field)
class ASTBuildListener(LLangListener):
    def enterEveryRule(self, ctx):
        ctx.ast = NonTerminalASTNode(get_rule_name(ctx))

    def exitEveryRule(self, ctx):
        if ctx.parentCtx:
            ctx.parentCtx.ast.addChild(ctx.ast)

    def exitIntLiteral(self, ctx):
        ctx.ast = IntASTNode(ctx.ast.getDeepestTerminal().name)

    def exitStrLiteral(self, ctx):
        ctx.ast = StringASTNode(ctx.ast.getDeepestTerminal().name)

    def exitBoolLiteral(self, ctx):
        ctx.ast = BoolASTNode(ctx.ast.getDeepestTerminal().name)

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