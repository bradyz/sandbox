from collections import Counter
o = 0
for v in Counter(input()).values():
    if v % 2 == 1:
        o += 1
if o <= 1:
    print("yes")
else:
    print("no")
