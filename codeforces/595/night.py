n, m = map(int, input().split())
windows = [list(map(int, input().split())) for _ in range(n)]
on = 0
for i in range(n):
    for j in range(m):
        on += windows[i][2*j] or windows[i][2*j+1]
print(on)
