# Design an algorithm and write code to remove the duplicate characters in a
# string without using any additional bufer.
# NOTE: One or two additional variables are fine.
# An extra copy of the array is not.

a = list("applesandoranges")
dupes = 0
b = set()

print("".join(a))

for i in range(len(a)):
    if a[i] in b:
        dupes += 1
        for j in range(i+1, len(a)):
            a[j-1] = a[j]
    else:
        b.add(a[i])

print("".join(a[:-dupes]))
