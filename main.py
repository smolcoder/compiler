from antlr4 import FileStream, CommonTokenStream
from ast import buildAST
from grammar.gen.LLangLexer import LLangLexer
from grammar.gen.LLangParser import LLangParser


input = FileStream('example.l')
lexer = LLangLexer(input)
stream = CommonTokenStream(lexer)
parser = LLangParser(stream)
tree = parser.programme()
ast = buildAST(tree)
