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
        cortege = '[Int, Str, Bool] c;'

        ca = self.getLeftHandSide(cortege + '\n{c[0] = 2;}')
        self.assertEqual(ca.type, 'Int')

        ca = self.getLeftHandSide(cortege + '\n{c[1] = "asdf";}')
        self.assertEqual(ca.type, 'Str')

        ca = self.getLeftHandSide(cortege + '\n{c[2] = false;}')
        self.assertEqual(ca.type, 'Bool')

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
                                      'p.info.addr.c[2] = "str";'
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

    def test_arithmetic(self):
        self.assertHasError('{Int i; i = true;')
        self.assertHasError('{Int i = "str";')
        self.assertHasError('{Bool f = false && 3')
        self.assertHasError('{Bool f = "str" && true')
        self.assertHasError('{Str s = "str" + "d"')
        self.assertHasError('{Str s = "str" + 3')
        self.assertHasError('{Str s = "str" + 3')
        self.assertHasNoError('{Bool f = ((((3 + 4))) * 5 > 3) && true || (1 < 0);}')

        self.assertHasNoError('Int result; Int a; Int c; Bool f = (result == 2) != !(a == -1) && (c >= 2);')
        self.assertHasError('Bool result; Int a; Int c; Bool f = (result == 2) != !(a == -1) && (c >= 2);')
        self.assertHasError('Int result; Str a; Int c; Bool f = (result == 2) != !(a == -1) && (c >= 2);')
        self.assertHasError('Int result; Int a; Bool c; Bool f = (result == 2) != !(a == -1) && (c >= 2);')

        self.assertHasNoError('{Int result; result += 1 + 2 * (3 + 4) - -5 / 6 % 7;}')
        self.assertHasNoError('{Int result; result -= 1 + 2 * (3 + 4) - -5 / 6 % 7;}')
        self.assertHasNoError('{Int result; result /= 1 + 2 * (3 + 4) - -5 / 6 % 7;}')
        self.assertHasNoError('{Int result; result %= 1 + 2 * (3 + 4) - -5 / 6 % 7;}')

        self.assertHasError('{Str result; result %= 1 + 2 * (3 + 4) - -5 / 6 % 7;}')
        self.assertHasError('{Bool result; result %= 1 + 2 * (3 + 4) - -5 / 6 % 7;}')
        self.assertHasError('{Int result; result == 1 + 2 * (3 + 4) - -5 / 6 % 7;}')
        self.assertHasError('{Int result; result >= 1 + 2 * (3 + 4) - -5 / 6 % 7;}')
        self.assertHasError('{Int result; result <= 1 + 2 * (3 + 4) - -5 / 6 % 7;}')

        self.assertHasNoError('fun foo(a: Int, b: Str): Int {return 0;} {Int i = -foo(1, "str") * 1;}')
        self.assertHasError('fun foo(a: Int, b: Str): [Int] {} {[Int, Int] i = foo(1, "str");}')

    def test_fun_arg_types(self):
        self.assertHasNoError('fun foo():None{} {foo();}')
        self.assertHasError('fun foo():None{} {foo(3);}')

        self.assertHasNoError('record Rec {Int i;}'
                              'fun foo(a:Int, b:Str, c:Rec, d:[Int, Bool, Str, Int]):None {}'
                              '{Str s; foo(1, s, new Rec(i=3), [1, true, "s", 2]);}')
        self.assertHasError('record Rec {Int i;}'
                            'fun foo(a:Int, b:Str, c:Int, d:[Int, Bool, Str, Int]):None {}'
                            '{Str s; foo(1, s, new Rec(i=3), [1, true, "s", 2]);}')
        self.assertHasError('record Rec {Int i;}'
                            'fun foo(a:Int, c:Rec, d:[Int, Bool, Str, Int]):None {}'
                            '{Str s; foo(1, s, new Rec(i=3), [1, true, "s", 2]);}')

        self.assertHasError('record Rec {Int i;}'
                            'fun foo(a:Int, b:Str, c:Rec, d:[Int, Bool, Str, Int]):None {}'
                            '{Str s; foo(1, s, new Rec(i=3), [1, 4, "s", 2]);}')

        self.assertHasError('record Rec {Int i;}'
                            'fun foo(a:Int, b:Str, c:Rec, d:[Int, Bool, Str, Int]):None {}'
                            '{Str s; foo(1, s, new Rec(i=3), [1, true, "s", 2], g: Int);}')

        self.assertHasError('record Rec {Int i;}'
                            'fun foo(a:Int, b:Str, c:Rec, d:[Int, Bool, Str]):None {}'
                            '{Str s; foo(1, s, new Rec(i=3), [1, true, "s", 2]);}')

    def test_record_init(self):
        self.assertHasNoError('record Rec{} {Rec r = new Rec();}')
        self.assertHasError('record Rec{} {Rec r = new Rec(i=3);}')

        self.assertHasNoError('record Rec{Int a; Str b; [Int, Bool] c;}'
                              '{Rec r = new Rec(a=1, b="str", c=[2, false]);}')
        self.assertHasNoError('record Rec{Int a; Str b; [Int, Bool] c;}'
                              '{Rec r = new Rec(b="str", a=1, c=[2, false]);}')
        self.assertHasNoError('record Rec{Int a; Str b; [Int, Bool] c;}'
                              'fun foo(r:Rec):None {}'
                              '{foo(new Rec(a=1, b="str", c=[2, false]));}')

        self.assertHasError('record Rec{Int a; Str b; [Int, Bool] c;}'
                            '{Rec r = new Rec(a=1, b="str", c=[2, "false"]);}')
        self.assertHasError('record Rec{Int a; Str b; [Int, Bool] c;}'
                            '{Rec r = new Rec(b="str", c=[2, false]);}')
        self.assertHasError('record Rec{Int a; Str b; [Int, Bool] c;}'
                            'fun foo(r:Rec):None {}'
                            '{foo(new Rec(a=1, b="str", c=[2, false], d=3));}')

    def test_if_statement(self):
        self.assertHasNoError('fun foo():Bool {return false;}'
                              '{Bool f;'
                              'if (foo() && f) {} '
                              'elif (3 > 4) {} '
                              'elif (false || foo()) {} '
                              'else {} '
                              '}')

        self.assertHasError('fun foo():Int {}'
                            '{Bool f;'
                            'if (foo()) {} '
                            'elif (3 > 4) {} '
                            'elif (false || foo()) {} '
                            'else {} '
                            '}')

        self.assertHasError('fun foo():Bool {}'
                            '{Bool f;'
                            'if (foo() && f) {} '
                            'elif (3 + 4) {} '
                            'elif (false || foo()) {} '
                            'else {} '
                            '}')

        self.assertHasError('fun foo():Bool {}'
                            '{Bool f;'
                            'if (foo() && f) {} '
                            'elif (3 > 4) {} '
                            'elif ("asf") {} '
                            'else {} '
                            '}')

        self.assertHasError('fun foo():Bool {}'
                            '{Bool f;'
                            'if (foo() && f) {} '
                            'elif (3 > 4) {} '
                            'elif () {} '
                            'else {} '
                            '}')

        self.assertHasError('fun foo():Bool {}'
                            '{Bool f;'
                            'if () {} '
                            'elif (3 > 4) {} '
                            'elif (false || foo()) {} '
                            'else {} '
                            '}')

    def test_for_condition(self):
        self.assertHasNoError('{for (Int i = 1; i < 10; i += 1) {}}')
        self.assertHasNoError('{for (Int i = 1; i == 10; i -= 3) {}}')
        self.assertHasNoError('{for (Int i = 1; i >= 10; i /= 5) {}}')
        self.assertHasError('fun foo():None {} {for (Int i = 1; foo(); i *= 5) {}}')
        self.assertHasError('fun foo(i: Int):Int {} {for (Int i = 1; foo(i); i *= 5) {}}')
        self.assertHasError('fun foo(i: Int):Str {} {for (Int i = 1; foo(i); i *= 5) {}}')
        self.assertHasError('fun foo(i: Int):[Bool] {} {for (Int i = 1; foo(i); i *= 5) {}}')
        self.assertHasNoError('fun foo(i: Int):Bool {return false;} {for (Int i = 1; foo(i); i *= 5) {}}')

    def test_return_type(self):
        self.assertHasError('fun foo():None {return 3;}')
        self.assertHasNoError('fun foo():None {}')
        self.assertHasError('fun foo():Str {}')
        self.assertHasError('fun foo():Int {return;}')
        self.assertHasError('fun foo():[Int, Int] {return 3;}')
        self.assertHasError('fun foo():[Int] {return 3;}')
        self.assertHasNoError('fun foo():[Int, Int] {return [3, 3];}')

        self.assertHasNoError('{}')
        self.assertHasError('{return 3;}')
        self.assertHasNoError('{if(true){return;}}')
