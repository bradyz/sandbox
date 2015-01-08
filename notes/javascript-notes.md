JavaScript Reference
-------------------------------------------------------------------------------

#####Author: B-rad

Table of Contents:
-------------------------------------------------------------------------------

1. Dictionaries

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
