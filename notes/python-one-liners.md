#Python One Liners 
-------------------------------------------------------------------------------

Return word with maximum frequency
```python
from collections import Counter
sorted(Counter(["cat", "cat", "cat", "dog", "pig", "pig"]), key=lambda x: x[1])[-1]
```

Stdin space delimited values to list of ints
```python
list(map(int, input().split()))
```

Reverse words in a sentence but not the order
```python
string = "i enjoy sleeping cats"
" ".join(map(lambda x: "".join(reversed(x)), s.split()))
```
