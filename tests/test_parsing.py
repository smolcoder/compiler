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
        self.assertHasError('{for(Int i = 0; i < 10; i += 1) readInt(i);}')
        self.assertHasNoError('{for(Int i = 0; i < 10; i += 1) {readInt(i);}}')

    def test_cortege_with_record(self):
        self.assertHasNoError('[Int, Str, Bool, [Int, Str]] ok;')
        self.assertHasError('[Int, Str, Bool, [Int, Str], SomeRecord] ok;')

    def test_none_type(self):
        self.assertHasError('None none;')

    def test_outer_block(self):
        self.assertHasError('Int i; i = 3;')
        self.assertHasNoError('Int i; {i = 3;}')
        self.assertHasNoError('fun foo():None {}')
        self.assertHasError('{}{}')
        self.assertHasNoError('{{}{}{}}')

    def test_for_statement(self):
        self.assertHasNoError('{for (Int i = 1; i < 10; i += 1) {}}')
        self.assertHasError('{for (Int i = 1; i = 10; i += 1) {}}')
        # self.assertHasNoError('{Int i; for (; i < 10; i += 1) {}}')
        # self.assertHasNoError('{Int i; for (;; i += 1) {}}')
        self.assertHasError('{for (Int i = 1; i >= 10; i * 5) {}}')