from antlr4 import FileStream
from ast import pprintAST
from compiler import Compiler

# todo  add checking for break and continue
# todo  make any semantic checking abstract
# todo  add checking clinit variables (using uninitialized variable)
from env import makeVariableTables
from generator.linker import makeTAD

from runner import runProgramme


def main():
    compiler = Compiler()
    result = compiler.compile(FileStream('_example.l'))
    if result.errors:
        result.printErrors()
    else:
        ast = result.ast
        makeVariableTables(ast)
        makeTAD(ast)

        # pprintAST(ast)
        print '\n'.join(map(str, makeTAD(ast)))
        print '_' * 50
        runProgramme(ast, 'Main', 'Main')

main()