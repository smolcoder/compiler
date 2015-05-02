from ast import pprintAST
from semantic.typechecker import getCortegeAccessType, getFieldAccessType
from tests import BaseTestCase


class TypeCheckerTestCase(BaseTestCase):
    def getCortegeAccess(self, code):
        result = self.compile(code)
        ast = result.ast
        return ast.filterByName('cortegeAccess')[0]

    def getCompileWithFile(self, code):
        data = open('source/record_access.llang').read() + code
        return self.compile(data)

    def test_all_record_types_exists(self):
        self.assertHasError('{Person p;}')
        self.assertHasError('record Person {Address a;}')

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

    def test_record_access_ok(self):
        res = self.getCompileWithFile('{'
                                         'Person p;'
                                         'p.info.addr.home = 3;'
                                         'p.info.addr.street = "lenin";'
                                         'p.info.addr = Address();'
                                         'p.info = Info();'
                                         'p.info.addr.c[0] = 2;'
                                         'p.info.addr.c[1][1] = "str";'
                                         '}')
        lhs = res.ast.filterByName('leftHandSide')

        self.assertEqual(getFieldAccessType(lhs[0].getFirstChild(), res.ast.env)[0], 'Int')
        self.assertEqual(getFieldAccessType(lhs[1].getFirstChild(), res.ast.env)[0], 'Str')
        self.assertEqual(getFieldAccessType(lhs[2].getFirstChild(), res.ast.env)[0], 'Address')
        self.assertEqual(getFieldAccessType(lhs[3].getFirstChild(), res.ast.env)[0], 'Info')
        self.assertEqual(getFieldAccessType(lhs[4].getFirstChild(), res.ast.env)[0], 'Int')
        self.assertEqual(getFieldAccessType(lhs[5].getFirstChild(), res.ast.env)[0], 'Str')

    def test_record_access_unknown_field(self):
        res = self.getCompileWithFile('{'
                                      'Person p;'
                                      'p.info.addr.no_such_field = 3;'
                                      '}')
        lhs = res.ast.filterByName('leftHandSide')
        self.assertIsNotNone(getFieldAccessType(lhs[0].getFirstChild(), res.ast.env)[1])

    def test_record_access_non_record(self):
        res = self.getCompileWithFile('{'
                                      'Person p;'
                                      'p.notRecord.field = 3;'
                                      '}')
        lhs = res.ast.filterByName('leftHandSide')
        self.assertIsNotNone(getFieldAccessType(lhs[0].getFirstChild(), res.ast.env)[1])