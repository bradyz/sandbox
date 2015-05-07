CS 371P Exam 2 Notes
=====

**Algorithms**
----
  + `int count(II a_s, II a_end, II b) const`
  + `bool equal(II a_s, II a_end, II b) const` ++ forward-list, list, vector
  + `void reverse(II a_s, II a_end)` ++, -- list, vector
  + `void sort(II a_s, II a_end)` \[  ] vector
  + `void fill(II start, II end, T val)`
  + `void swap(T a, T b)`
  + `II find(II start, II end, T val)`
  + `II remove(II start, II end, T val)`
  + `II reverse(II start, II end)`
  + `OI copy(II a_s, II a_end, II b)`

**Pointers**
----
  + `int* i` - R/W pointer must point at R/W target
  + `const int* i` - R pointer can point at R/W or R target
  + `int* const i` - R/W single target pointer can point point at R/W or R target 
  + `const int* const i` - R single target pointer must point a R target 

**Operators**
----
  + `bool operator==(cont range_iterator&)` - protects caller, allows r-value
  + `T& operator<<=(const T& rhs)`
  + `T& operator++()`
  + `T operator++(int)`
  + `T& operator[](size_t i)`

**R-Val/L-Val**
----
  + `int a[] = {1, 2, 3}` variable size declaration
  + `int a[5] = {1, 2, 3}` 5 int declaration, 2 other are 0
  + `a` - r-val array address
  + `a[0]` - l-val array element
  + `*(a + 1)` l-val array element

**Vector**
----
  + `void push_back(const T& val)`
  + `void pop_back()`
  + `insert(II position, const T& val)`
  + `size_t size() const`
  + `void erase(II i)`
  + `II begin()`
  + `II end()`
  + `T& operator[](size_t i)`

**Queue**
----
  + `bool empty() const`
  + `size_t size() const`
  + `T& front()`
  + `T& back()`
  + `void push(const T& val)`
  + `void pop()`

**Set**
----
  + `bool empty() const`
  + `II find(const T& val)`
  + `size_t size() const`
  + `void insert(const T& val)`
  + `void clear()`
  + `size_t count(const T& val) const`
  + `size_t erase(const T& val)`

**Stack**
----
  + `bool empty() const`
  + `size_t size() const`
  + `void pop()`
  + `T& top()`
  + `void push(const T& val)`

**List**
----
  + `bool empty() const`
  + `size_t size() const`
  + `void push_front(const T& val)`
  + `void push_back(const T& val)`
  + `void pop_front()`
  + `void pop_back()`
  + `T& back()`
  + `T& front()`
  + `II erase(II i)`
