# Implement an algorithm to determine if a string has all unique characters.
# What if you can not use additional data structures?

a = "string a bunch of characters"

for i, c in enumerate(sorted(a.replace(" ", ""))):
    if i == 0:
        prev = c
    else:
        if c == prev:
            print("Dupe found: " + str(c))
        prev = c

if len(set(a)) - len(a) != 0:
    print("Dupes found")
