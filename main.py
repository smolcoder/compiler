from antlr4 import FileStream
from ast import pprintAST
from compiler import Compiler


def main():
    compiler = Compiler()
    result = compiler.compile(FileStream('example.l'))
    if result.errors:
        result.printErrors()
    else:
        pass
        pprintAST(result.ast)

main()