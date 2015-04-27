from grammar.gen.LLangListener import LLangListener
from antlr4 import *
from utils import capitalizeFirst, getRuleName


class PrimitiveType:
    INT = 'Int'
    STR = 'Str'
    BOOL = 'Bool'


class TypedASTNode:
    def getType(self):
        pass


class ASTNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class TerminalASTNode(ASTNode):
    def __init__(self, name, value=None):
        ASTNode.__init__(self, name)
        self.value = value

    def getDeepest(self):
        return self

    def __str__(self):
        return '{}[{}]'.format(self.name, self.value) if self.value is not None else self.name


class NonTerminalASTNode(ASTNode):
    def __init__(self, name):
        ASTNode.__init__(self, name)
        self._children = []

    def getChildren(self):
        return self._children

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

    def getDeepest(self):
        if len(self._children) != 1:
            raise Exception('Node {} has two or more children.'.format(self))
        first = self.getFirstChild()
        return first if isinstance(first, TerminalASTNode) else first.getDeepest()


class ErrorASTNode(TerminalASTNode):
    def __init__(self, errorInfo):
        TerminalASTNode.__init__(self, 'Error')
        self.errorInfo = errorInfo


class LiteralASTNode(TerminalASTNode, TypedASTNode):
    _type = None

    def __init__(self, value):
        TerminalASTNode.__init__(self, self._type, value)

    def getType(self):
        return self._type


class StrLiteralASTNode(LiteralASTNode):
    _type = PrimitiveType.STR


class IntLiteralASTNode(LiteralASTNode):
    _type = PrimitiveType.INT


class BoolLiteralASTNode(LiteralASTNode):
    _type = PrimitiveType.BOOL


class IdASTNode(TerminalASTNode):
    def __init__(self, identifier):
        TerminalASTNode.__init__(self, 'Identifier', identifier)


class PrimitiveTypeASTNode(TerminalASTNode):
    def __init__(self, _type):
        TerminalASTNode.__init__(self, 'PrimitiveType', _type)


class OperatorASTNode(TerminalASTNode):
    pass


class ASTWalker:
    def buildEnterName(self, s):
        return 'enter' + capitalizeFirst(s)

    def buildExitName(self, s):
        return 'exit' + capitalizeFirst(s)

    def buildVisitName(self, s):
        return 'visit' + capitalizeFirst(s)

    def walk(self, listener, ast):
        if isinstance(ast, TerminalASTNode):
            name = self.buildVisitName(ast.name)
            if hasattr(listener, name):
                getattr(listener, name)(ast)
            elif hasattr(listener, 'visitTerminal'):
                getattr(listener, 'visitTerminal')(ast)
        self.enterNode(listener, ast)
        if isinstance(ast, NonTerminalASTNode):
            for c in ast.getChildren():
                self.walk(listener, c)
        self.exitNode(listener, ast)

    def enterNode(self, listener, ast):
        if hasattr(listener, 'enterEvery'):
            getattr(listener, 'enterEvery')(ast)
        cls = self.buildEnterName(ast.__class__.__name__)
        name = self.buildEnterName(ast.name)
        if hasattr(listener, name):
            getattr(listener, name)(ast)
        elif hasattr(listener, cls):
            getattr(listener, cls)(ast)

    def exitNode(self, listener, ast):
        cls = self.buildExitName(ast.__class__.__name__)
        name = self.buildExitName(ast.name)
        if hasattr(listener, name):
            getattr(listener, name)(ast)
        elif hasattr(listener, cls):
            getattr(listener, cls)(ast)
        if hasattr(listener, 'exitEvery'):
            getattr(listener, 'exitEvery')(ast)


def isTerminal(ast):
    return isinstance(ast, TerminalASTNode)


SKIP_SYMBOLS = ['[', ']', '{', '}', '(', ')', ';', ',', '.', ':',
                'fun', 'return', 'readln', 'writeln']

REMOVE_SEMICOLON_AFTER = [
    'variableDeclarationStatement',
    'passStatement',
    'returnStatement',
    'writelnStatement',
    'readlnStatement',
    'functionInvocationStatement',
    'assignmentStatement',
]

OPERATORS = [
    'unaryOperator',
    'mulDivModOperator',
    'addSubOperator',
    'compareOperator',
    'equalOrNotOperator',
    'boolOperator',
    'assignmentOperator'
]


# Builds AST node for each state context,
# binds it to the context (via making ast field)
class ASTBuildListener(LLangListener):
    def enterEveryRule(self, ctx):
        ctx.ast = NonTerminalASTNode(getRuleName(ctx))

    def exitEveryRule(self, ctx):
        ast = ctx.ast if ctx.ast.name not in REMOVE_SEMICOLON_AFTER else ctx.ast.getFirstChild()
        if ast.name in OPERATORS:
            ast = OperatorASTNode(capitalizeFirst(ast.name), ast.getFirstChild().value)
        if ctx.parentCtx:
            ctx.parentCtx.ast.addChild(ast)

    def exitIntLiteral(self, ctx):
        ctx.ast = IntLiteralASTNode(ctx.ast.getDeepest().value)

    def exitStrLiteral(self, ctx):
        ctx.ast = StrLiteralASTNode(ctx.ast.getDeepest().value)

    def exitBoolLiteral(self, ctx):
        ctx.ast = BoolLiteralASTNode(ctx.ast.getDeepest().value)

    def exitPrimitiveType(self, ctx):
        ctx.ast = PrimitiveTypeASTNode(ctx.ast.getDeepest().value)

    def exitIdentifier(self, ctx):
        ctx.ast = IdASTNode(ctx.ast.getDeepest().value)

    def visitTerminal(self, node):
        text = node.symbol.text
        if text in SKIP_SYMBOLS:
            return
        if node.parentCtx.ast.name == 'strLiteral':
            text = text[1:len(text) - 1]
        ast = TerminalASTNode('TerminalNode', text)
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


INDENT = '| '


def pprintAST(ast, indents=0):
    print indents * INDENT + str(ast)
    if isTerminal(ast):
        return
    for c in ast.getChildren():
        pprintAST(c, indents + 1)