from collections import deque

n = int(input())
l1 = deque(list(map(int, input().split()))[1:])
l2 = deque(list(map(int, input().split()))[1:])
res = 0

while l1 and l2:
    c1, c2 = l1.popleft(), l2.popleft()
    if res > 1000:
        break
    elif c1 > c2:
        l1.append(c2)
        l1.append(c1)
    else:
        l2.append(c1)
        l2.append(c2)
    res += 1

if res > 1000:
    print(-1)
elif l1:
    print(res, 1)
else:
    print(res, 2)
