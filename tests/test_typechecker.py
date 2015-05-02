from ast import pprintAST
from semantic.typechecker import getCortegeAccessType
from tests import BaseTestCase


class TypeCheckerTestCase(BaseTestCase):
    def getCortegeAccess(self, code):
        result = self.compile(code)
        ast = result.ast
        return ast.filterByName('cortegeAccess')[0]

    def test_cortege_access_type(self):
        ca = self.getCortegeAccess('[Int] c; {c[0] = 2;}')
        cat, e = getCortegeAccessType(ca)
        self.assertEqual(cat, 'Int')

        cortege = '[Int, [Str, Bool, [Int], [Bool, Str], Int], Str] c;'

        ca = self.getCortegeAccess(cortege + '\n{c[0] = 2;}')
        cat, e = getCortegeAccessType(ca)
        self.assertEqual(cat, 'Int')

        ca = self.getCortegeAccess(cortege + '\n{c[1][0] = 2;}')
        cat, e = getCortegeAccessType(ca)
        self.assertEqual(cat, 'Str')

        ca = self.getCortegeAccess(cortege + '\n{c[1][2][0] = 2;}')
        cat, e = getCortegeAccessType(ca)
        self.assertEqual(cat, 'Int')

        ca = self.getCortegeAccess(cortege + '\n{c[1][3][1] = 2;}')
        cat, e = getCortegeAccessType(ca)
        self.assertEqual(cat, 'Str')

    def test_cortege_access_out_of_bound(self):
        ca = self.getCortegeAccess('[Int] c; {c[1] = 2;}')
        cat, e = getCortegeAccessType(ca)
        self.assertIsNone(cat)
        self.assertIsNotNone(e)

        ca = self.getCortegeAccess('[Int, [Str, Int, [Bool]], Str] c; {c[1][2][1] = 2;}')
        cat, e = getCortegeAccessType(ca)
        self.assertIsNone(cat)
        self.assertIsNotNone(e)