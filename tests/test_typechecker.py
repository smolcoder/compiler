from errors import NameNotFoundError
from tests import BaseTestCase


class TypeCheckerTestCase(BaseTestCase):
    def getLeftHandSide(self, code):
        result = self.compile(code)
        ast = result.ast
        return ast.filterByName('leftHandSide')[0]

    def getCompileWithFile(self, code):
        data = open('source/record_access.llang').read() + code
        return self.compile(data)

    def test_cortege_access_type(self):
        ca = self.getLeftHandSide('[Int] c; {c[0] = 2;}')
        self.assertEqual(ca.type, 'Int')

        cortege = '[Int, [Str, Bool, [Int], [Bool, Str], Int], Str] c;'

        ca = self.getLeftHandSide(cortege + '\n{c[0] = 2;}')
        self.assertEqual(ca.type, 'Int')

        ca = self.getLeftHandSide(cortege + '\n{c[1][0] = 2;}')
        self.assertEqual(ca.type, 'Str')

        ca = self.getLeftHandSide(cortege + '\n{c[1][2][0] = 2;}')
        self.assertEqual(ca.type, 'Int')

        ca = self.getLeftHandSide(cortege + '\n{c[1][3][1] = 2;}')
        self.assertEqual(ca.type, 'Str')

    def test_cortege_access_out_of_bound(self):
        self.assertHasError('[Int] c; {c[1] = 2;}')
        self.assertHasError('[Int, [Str, Int, [Bool]], Str] c; {c[1][2][1] = 2;}')

    def test_record_access_ok(self):
        res = self.getCompileWithFile('{'
                                      'Person p;'
                                      'p.info.addr.home = 3;'
                                      'p.info.addr.street = "lenin";'
                                      'p.info.addr = new Address();'
                                      'p.info = new Info();'
                                      'p.info.addr.c[0] = 2;'
                                      'p.info.addr.c[1][1] = "str";'
                                      '}')
        lhs = res.ast.filterByName('leftHandSide')

        self.assertEqual(lhs[0].type, 'Int')
        self.assertEqual(lhs[1].type, 'Str')
        self.assertEqual(lhs[2].type, 'Address')
        self.assertEqual(lhs[3].type, 'Info')
        self.assertEqual(lhs[4].type, 'Int')
        self.assertEqual(lhs[5].type, 'Str')

    def test_record_access_unknown_field(self):
        self.assertHasError('{'
                            'Person p;'
                            'p.info.addr.no_such_field = 3;'
                            '}', NameNotFoundError)

    def test_record_access_non_record(self):
        self.assertHasError('{'
                            'Person p;'
                            'p.notRecord.field = 3;'
                            '}', NameNotFoundError)
