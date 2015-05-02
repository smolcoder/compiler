import unittest
from antlr4 import FileStream
from antlr4.InputStream import InputStream
from compiler import Compiler


class BaseTestCase(unittest.TestCase):
    compiler = Compiler()

    def compile(self, code):
        return self.compiler.compile(InputStream(code))

    def compileFile(self, filename):
        return self.compiler.compile(FileStream(filename))

    def assertHasError(self, code, _type=None):
        result = self.compile(code)
        self.assertIsNotNone(result.errors)
        self.assertNotEquals(len(result.errors), 0, 'There is no errors.')
        if _type:
            for e in result.errors:
                if isinstance(e, _type):
                    return
            self.assertFalse(True, 'No exception of type ' + str(_type))

    def assertHasNoError(self, code):
        result = self.compile(code)
        self.assertTrue(result.errors is None or len(result.errors) == 0,
                        'Errors are not empty: {}'.format(str(result.errors)))