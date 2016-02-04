n = int(input())
c = list(map(int, input().split()))
ret = set()
for x in c:
    for y in range(x, -1, -1):
        if y not in ret:
            ret.add(y)
            break
print(sum(ret))
