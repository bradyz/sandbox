r, c, n, k = map(int, input().split())
g = set([tuple(map(int, input().split())) for _ in range(n)])
ret = 0
for i in range(r):
    for j in range(c):
        for l in range(1, r-i+1):
            for w in range(1, c-j+1):
                count = 0
                for a in range(i, i+l):
                    for b in range(j, j+w):
                        if (a+1, b+1) in g:
                            count += 1
                if count >= k:
                    ret += 1
print(ret)
