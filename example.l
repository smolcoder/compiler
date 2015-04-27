// This is some code snippets in L language.
/*
Block comments are supported too.
*/

Int global_int;
Str global_str_init = "initialized string";
Bool bool = false;

// Corteges
[Int, Int] point = [2, 3];
[Int, Bool, Str, [Int, Bool]] multiTypeCortege;


// Records
record Person {
    Int age = 0;
    Str gender = "";
    Address address;
    [Int, Int, Str] passportInfo;
}

record Address {
    Int house;
    Str street;
}

{
    // Empty block
}

{
    Int global_int;
}

// empty operator
fun doNothing():None {
    pass;
}

fun pow(n:Int, k:Int):Int {
    Int r = 1;
    while (k > 0) {
        if (k % 2 == 1) {
            r *= n;
        } else {
            pass;
        }
        r *= r;
        k /= 2;
    }
    return r;
}

// Record usage
fun getPerson():Person {
    // inline initialization
    Person p = Person(age=15, gender="male", address=Address(house=2, street="Lenin"), passportInfo = getPassportInfo());
    // access
    p.age = 13;
    return p;
}

// Cortege example
fun getPassportInfo():[Int, Int, Str] {
    // initialization
    [Int, Int, Str] result = [1234, 567890, "UFMS"];
    // access
    result[0] = 4321;
    return result;
}

// Basic example
fun foo(a:Int, b:Int):Int {
    Address addr = Address(house=2, street="Lenin");
    Int result;
    Int c;
    readln(result, c);
    for (addr.house = 1; addr.house <= (a + b); addr.house += 3) {
        if (a + b == 0) {
            result = 2;
        } elif (a + b == 1) {
            if (a == -1) {
                result = 3;
            }
            result += 1 + 2 * (3 + 4) - -5 / 6 % 7;
        } else {
            result = 5;
        }
        Bool f = (result == 2) != !(a == -1) && (c >= 2);
        writeln(f);
    }
    return 1 + result * 3;
}
