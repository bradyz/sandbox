Python Quick Reference!
-------------------------------------------------------------------------------

#####Author: B-rad

Table of Contents:
-------------------------------------------------------------------------------

1. Dictionaries
2. Files
3. Lists
4. Miscellaneous
5. Random

Dictionaries
-------------------------------------------------------------------------------

**initialization** - hardcoding certain values

```python
pairs = {"}": "{", ")": "("}
```

**counter** - subclass of dicts for tallying

```python
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
  cnt[word] += 1
```

Miscellaneous
-------------------------------------------------------------------------------

**\_\_name__** - code will only execute if the current file is run,
used for testing if later the file is modularized and imported into a project
  
```python
if __name__ == "__main__":
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
