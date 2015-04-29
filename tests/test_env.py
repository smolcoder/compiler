from pprint import pprint
from ast import pprintAST
from tests import BaseTestCase


class NameCollisionTestCase(BaseTestCase):
    def test_variable(self):
        result = self.compile('Int i; Int i;')
        self.assertEquals(len(result.errors), 1)

        self.assertHasNoError('Int i; {Int i;}')

        result = self.compile('{while(true){Int i; Int i;}}')
        self.assertEquals(len(result.errors), 1)

        self.assertHasNoError('{while(3){Int i; {Int i;}}}')

    def test_function(self):
        result = self.compile('fun foo():None {}\nfun foo():None {}')
        self.assertEquals(len(result.errors), 1)

        result = self.compile('fun foo(a:Int):Str {}\nfun foo(b:Str):Int {}')
        self.assertEquals(len(result.errors), 1)

    def test_records(self):
        result = self.compile('record A{Int a; Int b = 3;}\nrecord A{Str s;}')
        self.assertEquals(len(result.errors), 1)

    def test_record_function(self):
        self.assertHasError('fun Person():None {}\nrecord Person{}')

    def test_function_variable(self):
        self.assertHasNoError('fun foo(): None {} Int foo;')


class EnvTestCase(BaseTestCase):
    def setUp(self):
        self.res = self.compileFile('source/resolution.llang')

    def test_global_env(self):
        env = self.res.ast.env
        self.assertIn('foo', env.functions)
        self.assertTrue(env.resolveFunction('bar'))
        self.assertIn('i', env.variables)
        self.assertTrue(env.resolveVariable('s'))
        self.assertIn('t', env.variables)
        self.assertIn('p', env.variables)
        self.assertIn('Person', env.records)
        self.assertTrue(env.resolveRecord('Person'))

        self.assertNotIn('p1', env.variables)
        self.assertFalse(env.resolveVariable('i1'))

    def test_resolve_1(self):
        ast = self.res.ast
        varDeclarations = ast.filterByName('variableDeclaration')

        self.assertNotEqual(varDeclarations[-1].getEnv().resolveVariable('p'), ast.env.resolveVariable('p'))
        self.assertNotEqual(varDeclarations[-1].getEnv().resolveVariable('i'), ast.env.resolveVariable('i'))
        self.assertEqual(varDeclarations[-1].getEnv().resolveVariable('i'), varDeclarations[-4].getEnv().resolveVariable('i'))

        self.assertNotEqual(varDeclarations[7].getEnv().resolveVariable('p'), ast.env.resolveVariable('p'))
        self.assertEqual(varDeclarations[3].getEnv().resolveVariable('i')['ast'], varDeclarations[3])
        self.assertEqual(varDeclarations[3].getEnv().resolveVariable('s'), ast.env.resolveVariable('s'))
        self.assertNotEqual(varDeclarations[5].getEnv().resolveVariable('i'), ast.env.resolveVariable('i'))
        self.assertNotEqual(varDeclarations[5].getEnv().resolveVariable('s'), ast.env.resolveVariable('s'))
        self.assertEqual(varDeclarations[5].getEnv().resolveVariable('t'), ast.env.resolveVariable('t'))

        self.assertNotEqual(varDeclarations[-6].getEnv().resolveVariable('p'), ast.env.resolveVariable('p'))