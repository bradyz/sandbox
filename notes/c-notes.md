#C/C++ Reference

####Author: B-rad

Table of Contents:
-------------------------------------------------------------------------------
1. Definitions
2. Miscellaneous
3. Numbers
4. Strings
5. Templates
6. Typedef
7. Vectors

Definitions
-------------------------------------------------------------------------------

**Singleton** - a class in which only one instance may be created

Miscellaneous
-------------------------------------------------------------------------------

**macro** - usually in all caps, used to define other functions

```c
#define SQUARE(x) (x*x)
```

**struct** - storage for member variables, default is public

```c
struct foo {
  int asdf
  char *bar
};
```

**class** -  storage for member variables, methods, default is private

```c++
class Foo
```


Strings
-------------------------------------------------------------------------------

**strcpy(dest, src)** - copies the string into the pointer pString

```c++
strcpy(pString, "Hello world."); 
```

**sprintf(dest, format, src)** - copies the number "number" into memory

```c++
sprintf(string, "%d", number); 
```

Numbers
-------------------------------------------------------------------------------

**>>** - halves the number with a bitwise shift by 1

```c++
20 >> 1
```

Templates
-------------------------------------------------------------------------------

**abs**- type "T", returns the absolute value of input "a"

```c++
template<typename T> T abs(T a) { return a < 0 ? -a : a;  }
```

**square** - squares the input "a"

```c++
template<typename T> T sqr(T a) { return a*a;  }
```

Typedef
-------------------------------------------------------------------------------

**define a type** - li short for long long, ld short for long double

```c++
typedef long long li;
typedef long double ld;
```

Vectors
-------------------------------------------------------------------------------

**initialization** - how to

```c++
int n = 100;
vector<int> a(n);
```

