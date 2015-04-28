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