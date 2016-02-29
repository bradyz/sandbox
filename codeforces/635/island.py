n = int(input())-1
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.remove(0)
b.remove(0)
ret = True
a_i = a.index(1)
b_i = b.index(1)
for i in range(n):
    if a[(a_i + i) % n] != b[(b_i + i) % n]:
        ret = False
        break
if ret:
    print("YES")
else:
    print("NO")
