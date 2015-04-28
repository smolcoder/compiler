from antlr4.error.ErrorListener import ErrorListener
from grammar.gen.LLangListener import LLangListener
from utils import capitalizeFirst, getRuleName, SourceInfo


class ASTNode:
    def __init__(self, name, source):
        self.name = name
        self.source = source

        self.left = None
        self.right = None
        self.parent = None
        self.root = None
        self.env = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def getEnv(self):
        if self.env is not None:
            return self.env
        return self.parent.getEnv() if self.parent else None

    def getRoot(self):
        if not self.root:
            self.root = self.parent.getRoot()
        return self.root


class TerminalASTNode(ASTNode):
    def __init__(self, name, source, value):
        ASTNode.__init__(self, name, source)
        self.value = value

    def getDeepest(self):
        return self

    def __str__(self):
        return '{}[{}]'.format(self.name, self.value) if self.value is not None else self.name


class NonTerminalASTNode(ASTNode):
    def __init__(self, name, source):
        ASTNode.__init__(self, name, source)
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

    def getLastChild(self):
        return self._children[-1]

    def getChild(self, index):
        return self._children[index]

    def getFirstChildByName(self, name):
        for c in self.getChildren():
            if c.name == name:
                return c
        return None

    def getDeepest(self):
        if len(self._children) != 1:
            raise Exception('Node {} has zero, two or more children.'.format(self))
        first = self.getFirstChild()
        return first if isinstance(first, TerminalASTNode) else first.getDeepest()


class FunctionSignatureASTNode(NonTerminalASTNode):
    def getName(self):
        return self.getFirstChild().value

    def getArguments(self):
        paramsNode = self.getFirstChildByName('functionParameterList')
        if not paramsNode:
            return []
        params = []
        for c in paramsNode.getChildren():
            params.append((c.getChild(0).value, c.getChild(1).type))
        return params

    def getReturnType(self):
        return self.getLastChild().getFirstChild().type


class VariableDeclarationASTNode(NonTerminalASTNode):
    def getType(self):
        return self.getFirstChild().type

    def getName(self):
        return self.getChild(1).value

    # todo getInitializer()?


class LiteralASTNode(TerminalASTNode):
    def __init__(self, source, value):
        TerminalASTNode.__init__(self, self.__class__.__name__[:-7], source, value)


class StrLiteralASTNode(LiteralASTNode):
    pass


class IntLiteralASTNode(LiteralASTNode):
    pass


class BoolLiteralASTNode(LiteralASTNode):
    pass


class IdASTNode(TerminalASTNode):
    def __init__(self, source, identifier):
        TerminalASTNode.__init__(self, 'Identifier', source, identifier)


class RecordIdASTNode(TerminalASTNode):
    def __init__(self, source, identifier):
        TerminalASTNode.__init__(self, 'RecordID', source, identifier)
        self.type = identifier


class PrimitiveTypeASTNode(TerminalASTNode):
    def __init__(self, source, value):
        TerminalASTNode.__init__(self, 'PrimitiveType', source, value)
        self.type = value


class CortegeTypeASTNode(NonTerminalASTNode):
    def __init__(self, name, source):
        NonTerminalASTNode.__init__(self, name, source)


class OperatorASTNode(TerminalASTNode):
    pass


class ProgrammeASTNode(NonTerminalASTNode):
    def __init__(self, source):
        NonTerminalASTNode.__init__(self, 'Programme', source)
        self.root = self


class ASTWalker:
    def buildEnterName(self, s):
        return 'enter' + capitalizeFirst(s)

    def buildExitName(self, s):
        return 'exit' + capitalizeFirst(s)

    def buildVisitName(self, s):
        return 'visit' + capitalizeFirst(s)

    def walk(self, listener, ast, *args, **kwargs):
        if isinstance(ast, TerminalASTNode):
            name = self.buildVisitName(ast.name)
            if hasattr(listener, name):
                getattr(listener, name)(ast, *args, **kwargs)
            elif hasattr(listener, 'visitTerminal'):
                getattr(listener, 'visitTerminal')(ast, *args, **kwargs)
        self.enterNode(listener, ast, *args, **kwargs)
        if isinstance(ast, NonTerminalASTNode):
            for c in ast.getChildren():
                self.walk(listener, c, *args, **kwargs)
        self.exitNode(listener, ast, *args, **kwargs)

    def enterNode(self, listener, ast, *args, **kwargs):
        if hasattr(listener, 'enterEvery'):
            getattr(listener, 'enterEvery')(ast, *args, **kwargs)
        cls = self.buildEnterName(ast.__class__.__name__)
        name = self.buildEnterName(ast.name)
        if hasattr(listener, name):
            getattr(listener, name)(ast, *args, **kwargs)
        elif hasattr(listener, cls):
            getattr(listener, cls)(ast, *args, **kwargs)

    def exitNode(self, listener, ast, *args, **kwargs):
        cls = self.buildExitName(ast.__class__.__name__)
        name = self.buildExitName(ast.name)
        if hasattr(listener, name):
            getattr(listener, name)(ast, *args, **kwargs)
        elif hasattr(listener, cls):
            getattr(listener, cls)(ast, *args, **kwargs)
        if hasattr(listener, 'exitEvery'):
            getattr(listener, 'exitEvery')(ast, *args, **kwargs)


def isTerminal(ast):
    return isinstance(ast, TerminalASTNode)


def getSource(ctx):
    return SourceInfo(firstPos=ctx.start.start, lastPos=ctx.stop.stop, line=ctx.start.line, column=ctx.start.column)

SKIP_SYMBOLS = ['[', ']', '{', '}', '(', ')', ';', ',', '.', ':',
                'fun', 'return', 'readln', 'writeln', 'record',
                'if', 'elif', 'else', 'for', 'while']

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
        ctx.ast = NonTerminalASTNode(getRuleName(ctx), source=getSource(ctx))
        if ctx.parentCtx and hasattr(ctx.parentCtx, 'ast'):
            ctx.ast.parent = ctx.parentCtx.ast

    def enterProgramme(self, ctx):
        # overwrite AST
        ctx.ast = ProgrammeASTNode(source=getSource(ctx))

    def exitEveryRule(self, ctx):
        ast = ctx.ast if ctx.ast.name not in REMOVE_SEMICOLON_AFTER else ctx.ast.getFirstChild()
        if ast.name in OPERATORS:
            ast = OperatorASTNode(capitalizeFirst(ast.name), source=getSource(ctx), value=ast.getFirstChild().value)
        if ctx.parentCtx:
            ctx.parentCtx.ast.addChild(ast)

    def enterFunctionSignature(self, ctx):
        ctx.ast = FunctionSignatureASTNode('functionSignature', getSource(ctx))

    def exitIntLiteral(self, ctx):
        ctx.ast = IntLiteralASTNode(getSource(ctx), ctx.ast.getDeepest().value)

    def exitStrLiteral(self, ctx):
        ctx.ast = StrLiteralASTNode(getSource(ctx), ctx.ast.getDeepest().value)

    def exitBoolLiteral(self, ctx):
        ctx.ast = BoolLiteralASTNode(getSource(ctx), ctx.ast.getDeepest().value)

    def exitPrimitiveType(self, ctx):
        ctx.ast = PrimitiveTypeASTNode(getSource(ctx), ctx.ast.getDeepest().value)

    def exitVoidType(self, ctx):
        ctx.ast = PrimitiveTypeASTNode(getSource(ctx), ctx.ast.getDeepest().value)

    def exitIdentifier(self, ctx):
        ctx.ast = IdASTNode(getSource(ctx), ctx.ast.getDeepest().value)

    def exitRecordId(self, ctx):
        ctx.ast = RecordIdASTNode(getSource(ctx), ctx.ast.getDeepest().value)

    def exitExprType(self, ctx):
        ctx.ast.type = ctx.ast.getFirstChild().type

    def enterTypeNonEmptyList(self, ctx):
        ctx.ast.type = []

    def exitCortegeType(self, ctx):
        ctx.ast.type = ctx.ast.getFirstChild().type

    def exitTypeNonEmptyList(self, ctx):
        for c in ctx.ast.getChildren():
            ctx.ast.type.append(c.type)

    def enterVariableDeclaration(self, ctx):
        ctx.ast = VariableDeclarationASTNode('variableDeclaration', getSource(ctx))
        ctx.ast.parent = ctx.parentCtx.ast

    def visitTerminal(self, node):
        symbol = node.symbol
        text = symbol.text
        source = SourceInfo(firstPos=symbol.start, lastPos=symbol.stop,
                            line=symbol.line, column=symbol.column)
        if text in SKIP_SYMBOLS:
            return
        if node.parentCtx.ast.name == 'strLiteral':
            text = text[1:len(text) - 1]
        ast = TerminalASTNode('TerminalNode', source, text)
        node.parentCtx.ast.addChild(ast)


INDENT = '| '


def pprintAST(ast, indents=0):
    print indents * INDENT + str(ast)
    if isTerminal(ast):
        return
    for c in ast.getChildren():
        pprintAST(c, indents + 1)


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append("Syntax error on line {}:{}: '{}'".format(line, column, offendingSymbol.text))