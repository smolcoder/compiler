from antlr4 import FileStream
from ast import pprintAST
from compiler import Compiler

# todo  add checking for break and continue
# todo  make any semantic checking abstract
# todo  add checking clinit variables (using uninitialized variable)
from generator.statement import bodyGenerator

from runner import runProgramme


def main():
    compiler = Compiler()
    result = compiler.compile(FileStream('_example.l'))
    if result.errors:
        result.printErrors()
    else:
        ast = result.ast
        pprintAST(ast)
        print '\n'.join(map(str, result.middleCode))
        print '_' * 50
        bc = bodyGenerator(ast.getJustBlock(), ast.lvt)
        print '\n'.join(bc)
        runProgramme(ast, 'Main', 'Main')
main()