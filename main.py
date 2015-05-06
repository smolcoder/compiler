from antlr4 import FileStream
from ast import pprintAST
from compiler import Compiler

# todo add checking for break and continue
# todo  make any semantic checking abstract
from generator import makeTAD, linkCode


def main():
    compiler = Compiler()
    result = compiler.compile(FileStream('_example.l'))
    if result.errors:
        result.printErrors()
    else:
        ast = result.ast
        # e = ast.filterByName('statement')
        # makeTAD(ast)
        # for i in e:
        #     print '\n'.join(linkCode(i))
        print '\n'.join(map(str, makeTAD(ast)))
        # pprintAST(ast)

main()