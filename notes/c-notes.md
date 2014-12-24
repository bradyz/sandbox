#C/C++ Quick Reference!

####Author: B-rad

Table of Contents:
-------------------------------------------------------------------------------
1. Definitions
2. Miscellaneous
3. Numbers
4. Strings

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

**sprintf(dest, format, src)** - copies the number "number" into the memory located at string

```c+
sprintf(string, "%d", number); 
```

Numbers
-------------------------------------------------------------------------------

**>>** - halves the number with a bitwise shift by 1

```c++
20 >> 1
```
