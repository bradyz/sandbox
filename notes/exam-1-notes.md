Java Notes
-----
1. ArrayList/LinkedList - use iterators that respond to next()
* For Each - used for code reusability as not all containers are indexable
* Non-Static Inner Class - tied to an instance
* Checked Exception - objects that use throws must be wrapped in try/catch
* <<= Operator - return is an r-val, left argument is an l-val

C++ Notes
-----
* Sizeof(arr) vs Sizeof(p)
  * Pointer - 8 bytes
  * Array - (number of T * sizeof(T)) bytes
* Algorithm Compatability
  * equal() - forward-list, list, vector
  * reverse() - list, vector 
  * sort() - vector
* Flavors of Pointers
  * int\* i - R/W pointer must point at R/W target
  * const int\* i - R pointer can point at R/W or R target
  * int\* const i - R/W single target pointer can point point at R/W or R target 
  * const int\* const i - R single target pointer must point a R target 
* Optimizations
  * bool operator==(cont range_iterator&) - protects caller, allows r-value
  * range_iterator& operator++() - return type is so that we can modify
  * range_iterator operator++(int) - returns an unmodifiable copy
* <<= Operator - return is an l-val, left argument is an l-val

Reading Notes
-----
1. Sapir-Whorf Hypothesis - the same things cannot be accomplished in every language
* Is-a vs. Has-a - specialization vs parts - interface vs inheritance
* The Open-Closed Principle - software entities should be open for extension but closed for modification
* C++ Orthodox Canonical Class Form
  * Default Constructor 
  * Copy Constructor 
  * Copy Assignment Operator 
  * Destructor
* Reasons to Use Inheritance 
  * implementation/interface 
  * code reuse/concept reuse
* Refinement Overriding vs. Replacement Overriding
  * replacement method replaces base version
  * refinement method runs in addition to base version
* Overloading
  * unchangeable properties - arity, associativity, precedence
* Assert
  * testing - inappropriate as failure kills program
  * user errors - inappropriate (see above) 
  * programmer errors - appropriate for developing purposes
* Nested Class - not tied to an instance
* Pair Programming - share a monitor and keyboard while coding
