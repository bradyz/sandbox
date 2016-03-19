n = int(input())
a = list(sorted(set(map(int, input().split()))))
n = len(a)
ret = False
for i in range(2, n):
    if a[i-2] + 1 == a[i-1] and a[i-1] + 1 == a[i]:
        ret = True
if ret:
    print("YES")
else:
    print("NO")
