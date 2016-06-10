n, k = map(int, input().split())
c = list(map(int, input().split()))
page = 1
r = 0
for v in c:
    for i in range(1, v+1):
        if i == page:
            r += 1
        if i % k == 0:
            page += 1
    if v % k != 0:
        page += 1
print(r)
