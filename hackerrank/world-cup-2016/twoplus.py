DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
best = 0
for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1+1, n):
            for y2 in range(y1+1, m):
                a, b = -1, -1
                a_set = set()
                for k in range(n):
                    new_a = {(x1 + k * dx, y1 + k * dy) for dx, dy in DIR}
                    a_bad = False
                    for xp, yp in new_a:
                        if xp < 0 or xp >= n or yp < 0 or yp >= m or \
                                grid[xp][yp] == "B":
                            a_bad = True
                    if a_bad:
                        break
                    a_set |= new_a
                    a = k
                for k in range(n):
                    new_b = {(x2 + k * dx, y2 + k * dy) for dx, dy in DIR}
                    b_bad = False
                    for xp, yp in new_b:
                        if xp < 0 or xp >= n or yp < 0 or yp >= m or \
                                grid[xp][yp] == "B" or (xp, yp) in a_set:
                            b_bad = True
                    if b_bad:
                        break
                    b = k
                if a >= 0 and b >= 0 and best < (1 + 4 * a) * (1 + 4 * b):
                    best = (1 + 4 * a) * (1 + 4 * b)
print(best)
