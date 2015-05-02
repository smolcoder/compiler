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
        self.assertHasError('{for(Int i = 0; i < 10; i += 1) readln(i);}')
        self.assertHasNoError('{for(Int i = 0; i < 10; i += 1) {readln(i);}}')

    def test_cortege_with_record(self):
        self.assertHasNoError('[Int, Str, Bool, [Int, Str]] ok;')
        self.assertHasError('[Int, Str, Bool, [Int, Str], SomeRecord] ok;')

    def test_left_hand_side(self):
        self.assertHasError('{[Int, Int] a; a[1].b = 2;}')
        self.assertHasNoError('record A {[Int, Int] b;} {A a; a.b[1] = 2;}')

    def test_none_type(self):
        self.assertHasError('None none;')

    def test_outer_block(self):
        self.assertHasError('Int i; i = 3;')
        self.assertHasNoError('Int i; {i = 3;}')
        self.assertHasNoError('fun foo():None {}')
        self.assertHasError('{}{}')
        self.assertHasNoError('{{}{}{}}')