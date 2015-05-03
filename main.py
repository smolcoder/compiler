from antlr4 import FileStream
from ast import pprintAST
from compiler import Compiler
from utils import jasmin, java, run


compiler = Compiler()
result = compiler.compile(FileStream('_example.l'))
if result.errors:
    result.printErrors()
else:
    pprintAST(result.ast)

# run('Greeter')