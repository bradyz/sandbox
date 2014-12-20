Python Quick Reference!
-------------------------------------------------------------------------------

#####Author: B-rad

Table of Contents:
-------------------------------------------------------------------------------

1. Dictionaries
2. Files
3. Lists
4. Miscellaneous

Miscellaneous
-------------------------------------------------------------------------------

code will only execute if the current file is run,
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

