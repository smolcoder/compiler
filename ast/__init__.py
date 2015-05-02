from errors import CompilerError, LLangSyntaxError
from antlr4.error.ErrorListener import ErrorListener
import sys
from grammar.gen.LLangListener import LLangListener
from grammar.gen.LLangParser import LLangParser
from utils import SourceInfo, getRuleName, capitalizeFirst
from nodes import *


def isTerminal(ast):
    return isinstance(ast, TerminalASTNode)


def getSource(ctx):
    return SourceInfo(firstPos=ctx.start.start, lastPos=ctx.stop.stop, line=ctx.start.line, column=ctx.start.column)


SKIP_SYMBOLS = ['[', ']', '{', '}', '(', ')', ';', ',', '.', ':',
                'fun', 'return', 'readln', 'writeln', 'record',
                'if', 'elif', 'else', 'for', 'while', 'new']

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

    def enterExpression(self, ctx):
        ctx.ast = ExpressionASTNode(getSource(ctx))

    def exitPrimitiveType(self, ctx):
        ctx.ast = PrimitiveTypeASTNode(getSource(ctx), ctx.ast.getDeepest().value)

    def exitLeftHandSide(self, ctx):
        if len(ctx.ast.getChildren()) == 1 and ctx.ast.getFirstChild().name == 'BoolLiteral':
            oldAst = ctx.ast
            ctx.ast = NonTerminalASTNode('literal', oldAst.source)
            ctx.ast.addChild(oldAst.getFirstChild())

    def exitVoidType(self, ctx):
        ctx.ast = PrimitiveTypeASTNode(getSource(ctx), ctx.ast.getDeepest().value)

    def exitIdentifier(self, ctx):
        value = ctx.ast.getDeepest().value
        if value in ['true', 'false']:
            ctx.ast = BoolLiteralASTNode(getSource(ctx), value)
        else:
            ctx.ast = IdASTNode(getSource(ctx), value)

    def enterElifBlock(self, ctx):
        ctx.ast = ElifBlockASTNode(getSource(ctx))

    def enterElseBlock(self, ctx):
        ctx.ast = ElseBlockASTNode(getSource(ctx))

    def exitRecordId(self, ctx):
        ctx.ast = RecordIdASTNode(getSource(ctx), ctx.ast.getDeepest().value)

    def exitExprType(self, ctx):
        ctx.ast.typeName = ctx.ast.getFirstChild().typeName

    def enterCortegeTypeNonEmptyList(self, ctx):
        ctx.ast.typeName = []

    def enterIfStatement(self, ctx):
        ctx.ast = IfStatementASTNode(getSource(ctx))

    def exitCortegeType(self, ctx):
        ctx.ast.typeName = ctx.ast.getFirstChild().typeName

    def exitCortegeTypeUnit(self, ctx):
        ctx.ast.typeName = ctx.ast.getFirstChild().typeName

    def exitCortegeTypeNonEmptyList(self, ctx):
        for c in ctx.ast.getChildren():
            ctx.ast.typeName.append(c.typeName)

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


def pprintAST(ast, indents=0, out=sys.stdout, indent='| '):
    out.write(indents * indent + str(ast) + '\n')
    if isTerminal(ast):
        return
    for c in ast.getChildren():
        pprintAST(c, indents + 1, out, indent)


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(LLangSyntaxError(offendingSymbol.text, SourceInfo(None, None, line, column)))


class ASTWalker:
    def buildEnterName(self, s):
        return 'enter' + capitalizeFirst(s)

    def buildExitName(self, s):
        return 'exit' + capitalizeFirst(s)

    def buildVisitName(self, s):
        return 'visit' + capitalizeFirst(s)

    def walk(self, listener, ast, *args, **kwargs):
        """
        :type listener: BaseASTListener
        """
        if isinstance(ast, TerminalASTNode):
            name = self.buildVisitName(ast.name)
            if hasattr(listener, name):
                getattr(listener, name)(ast, *args, **kwargs)
            else:
                listener.visitTerminal(ast, *args, **kwargs)
        self.enterNode(listener, ast, *args, **kwargs)
        if isinstance(ast, NonTerminalASTNode):
            for c in ast.getChildren():
                self.walk(listener, c, *args, **kwargs)
        self.exitNode(listener, ast, *args, **kwargs)

    def enterNode(self, listener, ast, *args, **kwargs):
        listener.enterEvery(ast, *args, **kwargs)
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
        listener.exitEvery(ast, *args, **kwargs)


class BaseASTListener:
    def visitTerminal(self, *args, **kwargs):
        pass

    def enterEvery(self, *args, **kwargs):
        pass

    def exitEvery(self, *args, **kwargs):
        pass

    def enterProgramme(self, *args, **kwargs):
        pass

    def exitProgramme(self, *args, **kwargs):
        pass


class NameFilterListener(BaseASTListener):
    def visitTerminal(self, ast, name, array, *args, **kwargs):
        if ast.name == name:
            array.append(ast)

    def enterEvery(self, ast, name, array, *args, **kwargs):
        if ast.name == name:
            array.append(ast)


def walkAST(listener, ast, *args, **kwargs):
    walker = ASTWalker()
    walker.walk(listener, ast, *args, **kwargs)