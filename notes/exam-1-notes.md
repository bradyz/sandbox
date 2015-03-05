CS 371P Exam 1 Notes
=====

C++ Notes
-----
1. **Sizeof(arr) vs Sizeof(p)**
  + Pointer - 8 bytes
  + Array - (number of T * sizeof(T)) bytes
* **Algorithm Compatability**
  + `equal()` - requires ++ (supported by forward-list, list, vector)
  + `reverse()` - requires ++, -- (supported by list, vector)
  + `sort()` - requires \[] (supported by vector)
* **Algorithms**
  + `copy()` - returns OI, two typenames (II, OI)
  + `count()` - returns int, two typesnames (II1, II2)
  + `equal()` - returns bool, two typenames (II1, II2)
  + `fill()` - returns void , two typenames (II, T)
  + `find()` - returns II, two typenames (II, T)
  + `remove()` - returns II, two typenames (II, T)
  + `reverse()` - returns II, one typename (II)
  + `swap()` - returns void, one typename (T)
* **Flavors of Pointers**
  + `int* i` - R/W pointer must point at R/W target
  + `const int* i` - R pointer can point at R/W or R target
  + `int* const i` - R/W single target pointer can point point at R/W or R target 
  + `const int* const i` - R single target pointer must point a R target 
* **Optimizations**
  + `bool operator==(cont range_iterator&)` - protects caller, allows r-value
  + `range_iterator& operator++()` - return type is & so that we can modify
  + `range_iterator operator++(int)` - returns a copy
* **Arrays**
  + `int a[]` - declaration
  + `a` - r-val address
  + `a[0]` - l-val element
  + `*(a + 1)` l-val element
* **Operators**
  + `<<=` - return is an l-val, left argument is an l-val
* **STL Containers**
  + Vector - push_back(), size()
  + Queue - empty(), size(), front(), back(), push_back(), pop_front()
  + Set - find(), size(), insert()
  + Stack - pop(), top(), push(), size()

Java Notes
-----
1. **ArrayList/LinkedList** - use iterators that respond to next()
* **For Each** - used for code reusability as not all containers are indexable
* **Non-Static Inner Class** - tied to an instance
* **Checked Exception** - objects that use throws must be wrapped in try/catch
* **Operators** 
  + `<<=`- return is an r-val, left argument is an l-val

Reading Notes
-----
1. **Sapir-Whorf Hypothesis** - the same things cannot be accomplished in every language
* **Is-a vs. Has-a** - specialization vs parts - interface vs inheritance
* **The Open-Closed Principle** - software entities should be open for extension but closed for modification
* **C++ Orthodox Canonical Class Form**
  + Default Constructor 
  + Copy Constructor 
  + Copy Assignment Operator 
  + Destructor
* **Reasons to Use Inheritance**
  + implementation/interface 
  + code reuse/concept reuse
* **Refinement Overriding vs. Replacement Overriding**
  + replacement method replaces base version
  + refinement method runs in addition to base version
* **Overloading**
  + unchangeable properties - arity, associativity, precedence
* **Assert**
  + testing - inappropriate as failure kills program
  + user errors - inappropriate (see above) 
  + programmer errors - appropriate for developing purposes
* **Nested Class** - not tied to an instance
* **Pair Programming** - share a monitor and keyboard while coding
