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

    def test_build_in(self):
        self.assertHasError('fun readln():None {}')
        self.assertHasError('fun writeln():None {}')


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
        self.assertNotIn('p', env.variables)
        self.assertIn('Person', env.records)
        self.assertTrue(env.resolveRecord('Person'))

        self.assertNotIn('p1', env.variables)
        self.assertFalse(env.resolveVariable('i1'))

    def test_resolve_1(self):
        ast = self.res.ast
        varDeclarations = ast.filterByName('variableDeclaration')

        i = varDeclarations[0]
        s = varDeclarations[1]
        t = varDeclarations[2]
        foo_i1 = varDeclarations[3]
        foo_s = varDeclarations[4]
        bar_s = varDeclarations[5]
        person_p = varDeclarations[6]
        block_i = varDeclarations[7]
        block_person_p = varDeclarations[8]
        block_block_block_p = varDeclarations[9]
        block_block_block_p1 = varDeclarations[10]

        self.assertEqual(s.getEnv(), ast.env)
        self.assertNotEqual(foo_s.getEnv().resolveVariable('s'), ast.env.resolveVariable('s'))
        self.assertNotEqual(foo_s.getEnv().resolveVariable('s'), bar_s.getEnv().resolveVariable('s'))
        self.assertIsNotNone(foo_s.getEnv().resolveVariable('i'))
        self.assertNotEqual(foo_s.getEnv().resolveVariable('i'), ast.env.resolveVariable('i'))
        self.assertNotEqual(foo_s.getEnv().resolveVariable('i'), bar_s.getEnv().resolveVariable('i'))
        self.assertIsNotNone(foo_s.getEnv().resolveVariable('i1'))
        self.assertIsNone(ast.env.resolveVariable('p'))
        self.assertIsNotNone(person_p.getEnv().resolveVariable('p'))
        self.assertNotEqual(person_p.getEnv().resolveVariable('p'), block_block_block_p.getEnv().resolveVariable('p'))
        self.assertNotEqual(block_person_p.getEnv().resolveVariable('p'), block_block_block_p.getEnv().resolveVariable('p'))
        self.assertNotEqual(block_person_p.getEnv().resolveVariable('p'), person_p.getEnv().resolveVariable('p'))
        self.assertIsNone(block_person_p.getEnv().resolveVariable('p1'))
        self.assertIsNone(ast.env.resolveVariable('p1'))
        self.assertNotEqual(ast.env.resolveVariable('i'), block_block_block_p1.getEnv().resolveVariable('i'))

    def test_resolve_build_in(self):
        res = self.compile('{Int a;}')
        var = res.ast.filterByName('variableDeclaration')[0]
        self.assertIsNotNone(var.getEnv().resolveBuildIn('readln'))
        self.assertIsNotNone(res.ast.getEnv().resolveFunction('writeln'))