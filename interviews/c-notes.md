#C/C++ Quick Reference!
##December 2014

Author: B-rad
-------------------------------------------------------------------------------

Table of Contents:
Miscellaneous
Numbers
Strings

Miscellaneous
-------------------------------------------------------------------------------
#define SQUARE(x) ((x)*(x))
  a macro, usually in all caps, used to define other functions

struct {};
  storage for member variables, default is public

class Foo
  storage for member variables, methods, default is private

Singleton 
  a class in which only one instance may be created

Strings
-------------------------------------------------------------------------------
strcpy(pString, "Hello world."); 
  copies the string into the pointer pString

sprintf(string, "%d", number); 
  copies the number "number" into the memory located at string

Miscellaneous
-------------------------------------------------------------------------------
20 >> 1
  halves the number with a bitwise shift by 1

