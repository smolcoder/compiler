import unittest
from antlr4.InputStream import InputStream
from compiler import Compiler


class ParsingTestCase(unittest.TestCase):
    compiler = Compiler()

    def compile(self, code):
        return self.compiler.compile(InputStream(code))

    def assertHasError(self, code):
        result = self.compile(code)
        self.assertTrue(result.errors)

    def assertHasNoError(self, code):
        result = self.compile(code)
        self.assertFalse(result.errors)

    def test_for_out_of_any_block(self):
        self.assertHasError('for(Int i = 0; i < 10; i += 1){}')

    def test_inc(self):
        self.assertHasError('{for(Int i = 0; i < 10; i++){}}')

    def test_empty_block(self):
        self.assertHasNoError('{}')

    def test_record_in_block(self):
        self.assertHasError('{record Rec{Int a; Int b;}}')

    def test_for_with_braces(self):
        self.assertHasError('{for(Int i = 0; i < 10; i += 1) print(x);}')
        self.assertHasNoError('{for(Int i = 0; i < 10; i += 1) {print(x);}}')

