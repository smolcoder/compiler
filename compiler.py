from antlr4 import CommonTokenStream, ParseTreeWalker
from ast import ASTBuildListener, SyntaxErrorListener
from env import buildEnv
from grammar.gen.LLangLexer import LLangLexer
from grammar.gen.LLangParser import LLangParser
from typechecker import TypeCheckListener, typeCheck


class CompilerResult:
    def __init__(self, ast=None, bytecode=None, errors=None, globalEnv=None):
        self.ast = ast
        self.globalEnv = globalEnv
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
        walker.walk(listener, rootRule)  # todo what errors?
        return rootRule.ast, []

    def compile(self, stream):
        programmeRule, parseErrors = self.parse(stream)
        if parseErrors:
            return CompilerResult(errors=parseErrors)

        ast, astBuildErrors = self.buildAST(programmeRule)
        if astBuildErrors:
            return CompilerResult(ast=ast, errors=astBuildErrors)

        globalEnv, envErrors = buildEnv(ast)
        if envErrors:
            return CompilerResult(ast=ast, globalEnv=globalEnv, errors=envErrors)

        typeErrors = self.typeCheck(ast, globalEnv)
        if typeErrors:
            return CompilerResult(ast=ast, globalEnv=globalEnv, errors=typeErrors)

        return CompilerResult(ast=ast, globalEnv=globalEnv)

    def typeCheck(self, ast, env):
        return typeCheck(ast, env)