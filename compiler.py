from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from ast import ASTBuildListener
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
        parser._listeners = []
        return parser.programme()

    def buildAST(self, rootRule):
        listener = ASTBuildListener()
        walker = ParseTreeWalker()
        walker.walk(listener, rootRule)
        ast = rootRule.ast
        errors = []
        if ast.errorNodes:
            template = 'Syntax error on line {}, column {}.'
            for node in ast.errorNodes:
                errors.append(template.format(node.source.line, node.source.column))
        return rootRule.ast, errors

    def compile(self, filename):
        stream = FileStream(filename)
        programmeRule = self.parse(stream)
        ast, errors = self.buildAST(programmeRule)
        return CompilerResult(ast=ast, errors=errors)