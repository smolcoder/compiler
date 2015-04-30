// This is some code snippets in L language.
/*
Block comments are supported too.
*/

Int global_int;
Int global_int_init = 3;
Str global_str_init = "initialized string";
Bool bool = false;

// Corteges
[Int, Int] point = [2, 3];
[Int, Bool, Str,
        [Int,
                Bool]] multiTypeCortege;


// Records
record Person {
    Int age = 0;
    Str gender = "";
    Address address;
    [Int, Int, Str] passportInfo;
}

Person person;

record Address {
    Int house;
    Str street;
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
    p.age.a = 14;
    p.age.b[1] = 15;
    {
        {
            // Empty block
        }
        Int global_int;
        {
            Str nested = "variable in the nested block";
        }
    }
    return p;
}

// Cortege example
fun getPassportInfo(asdf: [Int, [Str, Bool]]):[Int, Int, Str] {
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


{
    a.b.c = 1;
    a.b.c[1] = 2;
}