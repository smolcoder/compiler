# L language compiler
Simple L language compiler (compilers course at ITMO University).

## Some features
Supported buil-in types: Int, Bool, Str, Cortege. (None type for functions retures nothing).
You can declare/define both global and local variables:
```scala
// Primitive types
Int integer1;
Int integer2 = 2;
Bool f = false;
Str str = "some str";

// Cortege type
[Int, Str, Bool, [Int, Int]] cortege = [1, "str", true, [2, 3]];


fun foo():None {
  Int localVariable;
}
```
You can define your own type via records: 
```scala
record Address {
  Int house;
  Str street;
  [Int, Int] coords;
}
```
and use it:
```scala
Address address = Address(house=10, street="Lenin", coords=[1234, 5678]);

fun transformAddress(a:Address):Address {
  a.house = 2;
  a.coords[0] = 0;
  //...
}
```
See [fool example](https://github.com/smolcoder/compiler/blob/master/example.l)
