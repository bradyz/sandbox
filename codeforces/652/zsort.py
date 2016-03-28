n = int(input())
a = list(sorted(map(int, input().split())))
ret = list()
i = 0
j = n-1
while i <= j:
    if i != j:
        ret.append(a[i])
    ret.append(a[j])
    i += 1
    j -= 1
can = True
for i in range(1, n, 2):
    if ret[i] < ret[i-1]:
        can = False
if can:
    print(" ".join(map(str, ret)))
else:
    print("Impossible")
