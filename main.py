from compiler.misc import Stack
from antlr4 import FileStream, CommonTokenStream
from ast import buildAST, ASTWalker, pprintAST
from grammar.gen.LLangLexer import LLangLexer
from grammar.gen.LLangParser import LLangParser
from env import BuildEnvListener, buildEnv


def parse(filename):
    lexer = LLangLexer(FileStream(filename))
    stream = CommonTokenStream(lexer)
    parser = LLangParser(stream)
    return parser.programme()

root = parse('example.l')
ast = buildAST(root)
ast = buildEnv(ast)

pprintAST(ast)