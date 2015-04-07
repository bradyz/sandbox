# Write code to reverse a C-Style String. (C-String means that “abcd” is
# represented as five characters, including the null character.)

a = ["a", "s", "d", "f", None]

bi = 0
ei = len(a) - 2

while bi < ei:
    a[bi], a[ei] = a[ei], a[bi]
    bi += 1
    ei -= 1

print(a)
