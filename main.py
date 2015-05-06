from antlr4 import FileStream
from ast import pprintAST
from compiler import Compiler

# todo  add checking for break and continue
# todo  make any semantic checking abstract
# todo  add checking clinit variables (using uninitialized variable)
from env import makeVariableTables

from generator import makeTAD, linkCode
from generator.clinit import ClinitGenerator


def main():
    compiler = Compiler()
    result = compiler.compile(FileStream('_example.l'))
    if result.errors:
        result.printErrors()
    else:
        ast = result.ast
        makeVariableTables(ast)
        makeTAD(ast)
        # e = ast.filterByName('statement')
        # makeTAD(ast)
        # for i in e:
        #     print '\n'.join(linkCode(i))
        # print '\n'.join(map(str, makeTAD(ast)))
        cg = ClinitGenerator(ast)
        cg.generate()
        # pprintAST(ast)

main()