a = [list(input()) for _ in range(2)]
b = [list(input()) for _ in range(2)]
a = [a[0][0], a[0][1], a[1][1], a[1][0]]
b = [b[0][0], b[0][1], b[1][1], b[1][0]]
a.remove("X")
b.remove("X")
x = a.index("A")
y = b.index("A")
ret = True
for i in range(3):
    if a[(x + i) % 3] != b[(y + i) % 3]:
        ret = False
if ret:
    print("YES")
else:
    print("NO")
