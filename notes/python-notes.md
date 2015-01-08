Python Quick Reference!
-------------------------------------------------------------------------------

#####Author: B-rad

Table of Contents:
-------------------------------------------------------------------------------

1. Dictionaries
2. Files
3. Lists
4. Loops
5. matplotlib
6. Miscellaneous
7. Numpy
8. Random
9. Threads
10. Strings
11. Overloading

Dictionaries
-------------------------------------------------------------------------------

**initialization** - hardcoding certain values

```python
pairs = {"}": "{", ")": "("}
```

**counter** - subclass of dicts for tallying

```python
from collections import Counter
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
  cnt[word] += 1
```

Files
-------------------------------------------------------------------------------

turns the given file into an iterable

```python
with open('input.txt', 'r') as f:
  lines = f.readlines()
```

Lists and Arrays
-------------------------------------------------------------------------------

**sort()** - sorts the array in place

```python
arr.sort()
```

**len(src)** - returns the length of array

```python
len(arr)
```

**string array** - returns an array of strings split by spaces 

```python
line = [str(n) for n in x.split()]
```

**check empty array** - pythony way

```python
if not arr
```

Loops
-------------------------------------------------------------------------------

**conventional for loop** - python way!

```python
for i in range(len(arr)):
```

matplotlib
-------------------------------------------------------------------------------

**convention** - plt

```python
import matplotlib.pyplot as plt
```

**basic plotting** - provide x,y points and type of dots

```python```
x = [1, 2, 3]
y = [1, 2, 3]
plt.plot(x, y, 'ro')
plt.show()
```

Miscellaneous
-------------------------------------------------------------------------------

**\_\_name__** - code will only execute if the current file is run,
used for testing if later the file is modularized and imported into a project
  
```python
if __name__ == "__main__":
```

**timeit** - runs a snippet of code N times and finds the average

```python
from timeit import timeit
timeit("2 + 2")
```

**max, min int** - maximum and minumum integer values

```python
import sys
sys.maxint
min = -sys.maxint - 1
```

Numpy
-------------------------------------------------------------------------------

**grid** - init a bitmap grid

```python
import numpy as np
grid = np.zeros([rows, cols])
for i in range(rows):
    for j in range(cols):
        grid[i][j] = round(random.random())
return grid
```


Random
-------------------------------------------------------------------------------

**shuffle()** - shuffles the list in place using Fisher-Yates, O(n)

```python
shuffle(arr)
```

**random list** - list of random ints

```python
from random import randrange
L = [randrange(10000) for i in range(1000)]
```

Threads
-------------------------------------------------------------------------------

**initialization** - creates N threads to do a function with args

```python
for x in range(10):
  t = threading.Thread(name="Thread " + str(x), target=inc_n, args=(10,))
```

**start and join** - starts the thread of execution and reaps

```python
for x in range(len(threads)):
    threads[x].start()

for x in range(len(threads)):
    threads[x].join()
```

Strings
-------------------------------------------------------------------------------

**strip trailing/heading** - removes characters from the sides of the string

```python
str = "asdf\n"
str.strip('\n')
# str => "asdf"
```

Overloading
-------------------------------------------------------------------------------

**[] overload** - use the [] operator

```python
def __getitem__(self, index):
  return self.my_arr[index]
```
