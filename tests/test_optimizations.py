from ast import pprintAST
from tests import BaseTestCase


class OptimizationTestCase(BaseTestCase):
    def test_const_precalculation(self):
        res = self.compile(
            '{Bool i = (1 + ((2 - 1)) * 3) / 2 - -1 + (1 + 1) / 5 % 3 == 3 && !true || '
            '((3 > 2) && (1 < 3) && (true != false) && "a" == "a" && "a" != "b");}')
        literals = res.ast.filterByName('BoolLiteral')
        self.assertEqual(len(literals), 1)
        self.assertEqual(literals[0].value, 'true')

        res = self.compile('{Int i = ((1 + ((2 - 1)) * 3) / 2 - -1 + (1 + 1) / 5) % 2;}')
        literals = res.ast.filterByName('IntLiteral')
        self.assertEqual(len(literals), 1)
        self.assertEqual(literals[0].value, '1')