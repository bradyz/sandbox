n = int(input())
l = [1 if x == ">" else -1 for x in input()]
c = list(map(int, input().split()))
for i in range(len(c)):
    l[i] *= c[i]
ret = True
i = 0
vis = {i}
while True:
    if i < 0 or i >= n:
        ret = False
        break
    i += l[i]
    if i in vis:
        ret = True
        break
    vis.add(i)
if ret:
    print("INFINITE")
else:
    print("FINITE")
