from antlr4 import FileStream
from ast import pprintAST
from compiler import Compiler


compiler = Compiler()
result = compiler.compile(FileStream('example.l'))
if result.errors:
    result.printErrors()
else:
    pprintAST(result.ast)