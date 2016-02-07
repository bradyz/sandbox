from collections import deque
a = list(input())
b = list(input())
d = deque()
ret = 0
for i in range(min(len(b)-1, len(a))):
    d.append(a[i])
for i in range(len(b)-1, len(a)):
    d.append(a[i])
    if len(d) > len(b):
        d.popleft()
    remove = len(d) == len(b)
    if remove:
        for j in range(len(d)):
            if d[j] != b[j]:
                remove = False
                break
    if remove:
        ret += 1
        d.clear()
print(ret)
