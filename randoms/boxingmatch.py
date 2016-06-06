from Queue import Queue
n = int(input())
grid = [list(raw_input()) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
q = Queue()
for i in range(n):
    for j in range(n):
        if grid[i][j] == ".":
            dp[i][j] = 1
            q.put((i, j))
while not q.empty():
    x, y = q.get()
    if x == 0 or y == 0:
        continue
    can = True
    for dx, dy in [(-1, 0), (0, -1), (-1, -1)]:
        if dp[x+dx][y+dy] < dp[x][y]:
            can = False
    if can:
        dp[x][y] += 1
        q.put((x, y))
print("\n".join(map(str, grid)))
print("\n".join(map(str, dp)))
print(max(max(x) for x in dp))
