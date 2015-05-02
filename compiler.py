from antlr4 import CommonTokenStream, ParseTreeWalker

from ast import ASTBuildListener, SyntaxErrorListener
from env import buildEnv
from errors import CompilerError
from grammar.gen.LLangLexer import LLangLexer
from grammar.gen.LLangParser import LLangParser
from semantic import checkOnlyOneOuterJustBlock
from semantic.typechecker import typeCheck, checkAllRecordTypesExist


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
        walker.walk(listener, rootRule)
        ast, errors = rootRule.ast, []
        if not checkOnlyOneOuterJustBlock(ast):
            errors.append(CompilerError('Program has more than one outer block'))
        return ast, errors

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

        recTypeErrors = checkAllRecordTypesExist(ast)
        if recTypeErrors:
            return CompilerResult(ast=ast, globalEnv=globalEnv, errors=recTypeErrors)

        # typeErrors = self.typeCheck(ast, globalEnv)
        # if typeErrors:
        #     return CompilerResult(ast=ast, globalEnv=globalEnv, errors=typeErrors)

        return CompilerResult(ast=ast, globalEnv=globalEnv)

    def typeCheck(self, ast, env):
        return typeCheck(ast, env)