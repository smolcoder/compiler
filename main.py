from compiler import Compiler


compiler = Compiler()
result = compiler.compile('example.l')
if result.errors:
    result.printErrors()