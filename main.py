from antlr4 import FileStream
from ast import pprintAST
from compiler import Compiler

# todo add checking for break and continue
# todo  make any semantic checking abstract
from generator import makeTAD


def main():
    compiler = Compiler()
    result = compiler.compile(FileStream('_example.l'))
    if result.errors:
        result.printErrors()
    else:
        ast = result.ast
        # print '\n'.join(makeTAD(ast))
        pprintAST(ast)

main()