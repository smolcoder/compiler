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

        self.assertHasError('{while(true){Int i; {Int i;}}}')

        self.assertHasError('{Int i; for(Int i = 0; i < 10; i += 1}{}')
        self.assertHasNoError('{for(Int i = 0; i < 10; i += 1){} Int i;}')

        self.assertHasError('fun foo(a:Int, a:Int):None {}')
        self.assertHasError('{Int a; Int a;}')

    def test_function(self):
        self.assertHasError('fun foo():None {}\nfun foo():None {}')
        self.assertHasError('fun foo():None {}\nfun foo(a: Int):None {}')
        self.assertHasError('fun foo(a:Int):Str {}\nfun foo(b:Str):Int {}')

    def test_records(self):
        self.assertHasError('record A{Int a; Int b = 3;}\nrecord A{Str s;}')

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

        self.assertEqual(s.getEnv(), ast.env)
        self.assertNotEqual(foo_s.getEnv().resolveVariable('s'), ast.env.resolveVariable('s'))
        self.assertNotEqual(foo_s.getEnv().resolveVariable('s'), bar_s.getEnv().resolveVariable('s'))
        self.assertIsNotNone(foo_s.getEnv().resolveVariable('i'))
        self.assertNotEqual(foo_s.getEnv().resolveVariable('i'), ast.env.resolveVariable('i'))
        self.assertNotEqual(foo_s.getEnv().resolveVariable('i'), bar_s.getEnv().resolveVariable('i'))
        self.assertIsNotNone(foo_s.getEnv().resolveVariable('i1'))
        self.assertIsNone(ast.env.resolveVariable('p'))
        self.assertIsNotNone(person_p.getEnv().resolveVariable('p'))
        self.assertNotEqual(block_person_p.getEnv().resolveVariable('p'), person_p.getEnv().resolveVariable('p'))
        self.assertIsNone(block_person_p.getEnv().resolveVariable('p1'))
        self.assertIsNone(ast.env.resolveVariable('p1'))

    def test_resolve_build_in(self):
        res = self.compile('{Int a;}')
        var = res.ast.filterByName('variableDeclaration')[0]
        self.assertIsNotNone(var.getEnv().resolveBuildIn('readln'))
        self.assertIsNotNone(res.ast.getEnv().resolveFunction('writeln'))

    def test_lvt_mainblock(self):
        res = self.compile('Int n; {Int i; {Int j; {Int k;}} for (Int t = 0; t < 10; t += 1){}}')
        lvt = res.ast.getJustBlock().getLVT()
        self.assertIn('i', lvt.table)
        self.assertIn('j', lvt.table)
        self.assertIn('k', lvt.table)
        self.assertIn('t', lvt.table)
        self.assertNotIn('n', lvt.table)

    def test_lvt_fun(self):
        res = self.compile('Int t; fun foo(i:Int, s:Str):None {Int j;}')
        lvt = res.ast.filterByName('functionDeclaration')[0].getLVT()
        self.assertIn('i', lvt.table)
        self.assertIn('j', lvt.table)
        self.assertIn('s', lvt.table)
        self.assertNotIn('t', lvt.table)

    def test_lvt_global(self):
        res = self.compile('Int t; fun foo(i:Int, s:Str):None {Int j;}')
        lvt = res.ast.getLVT()
        self.assertNotIn('i', lvt.table)
        self.assertNotIn('j', lvt.table)
        self.assertNotIn('s', lvt.table)
        self.assertIn('t', lvt.table)