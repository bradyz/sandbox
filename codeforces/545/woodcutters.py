n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]
r = min(2, len(c))

for i in range(1, n-1):
    if c[i][0]-c[i][1] > c[i-1][0]:
        r += 1
    elif c[i][0]+c[i][1] < c[i+1][0]:
        c[i][0] += c[i][1]
        r += 1

print(r)
