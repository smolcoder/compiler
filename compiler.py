from antlr4 import CommonTokenStream, ParseTreeWalker
from ast import ASTBuildListener, SyntaxErrorListener
from grammar.gen.LLangLexer import LLangLexer
from grammar.gen.LLangParser import LLangParser


class CompilerResult:
    def __init__(self, ast=None, bytecode=None, errors=None):
        self.ast = ast
        self.bytecode = bytecode
        self.errors = errors

    def printErrors(self):
        if self.errors:
            for e in self.errors:
                print e


class Compiler:
    def parse(self, stream):
        lexer = LLangLexer(stream)
        stream = CommonTokenStream(lexer)
        parser = LLangParser(stream)
        errorListener = SyntaxErrorListener()
        parser._listeners = []  # bad code
        parser.addErrorListener(errorListener)
        return parser.programme(), errorListener.errors

    def buildAST(self, rootRule):
        listener = ASTBuildListener()
        walker = ParseTreeWalker()
        walker.walk(listener, rootRule)
        # if ast.errorNodes:
        #     template = 'Error on line {}, column {}.'
        #     for node in ast.errorNodes:
        #         errors.append(template.format(node.source.line, node.source.column))
        return rootRule.ast, []

    def compile(self, stream):
        programmeRule, parseErrors = self.parse(stream)
        if parseErrors:
            return CompilerResult(errors=parseErrors)

        ast, errors = self.buildAST(programmeRule)
        return CompilerResult(ast=ast, errors=errors)