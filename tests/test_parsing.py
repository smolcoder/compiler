from tests import BaseTestCase


class ParsingTestCase(BaseTestCase):
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

