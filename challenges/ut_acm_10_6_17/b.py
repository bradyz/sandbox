n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

s = float('inf')
t = -float('inf')

for i in range(n):
    for j in range(n):
        valid = True
        total = 0

        for x in range(k):
            for y in range(k):
                if i + x >= n or j + y >= n:
                    valid = False
                    continue

                total += grid[i+x][j+y]

        if valid:
            s = min(s, total / (k * k))
            t = max(t, total / (k * k))

print(t - s)
