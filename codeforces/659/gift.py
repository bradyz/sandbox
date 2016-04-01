n, m = map(int, input().split())
a = set(map(int, input().split()))
ret = list()
t = 1
while True:
    if m < t:
        break
    if t not in a:
        m -= t
        ret.append(t)
    t += 1
print(len(ret))
if ret:
    print(" ".join(map(str, ret)))
