from antlr4 import FileStream
from ast import pprintAST
from compiler import Compiler
from generator import recordAccessCode, linkCode, makeTAD
from semantic.optimizations import precalculateConstants


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