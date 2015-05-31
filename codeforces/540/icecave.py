from queue import Queue

n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]
s_x, s_y = map(int, input().split())
e_x, e_y = map(int, input().split())
ok = False

g[s_x-1][s_y-1] = "."
q = Queue()
q.put((s_x-1, s_y-1))

while not q.empty():
    cur = q.get()
    if cur[0] >= 0 and cur[0] < n and cur[1] >= 0 and cur[1] < m:
        if g[cur[0]][cur[1]] == ".":
            g[cur[0]][cur[1]] = "X"
            q.put((cur[0], cur[1]+1))
            q.put((cur[0], cur[1]-1))
            q.put((cur[0]+1, cur[1]))
            q.put((cur[0]-1, cur[1]))
        elif g[cur[0]][cur[1]] == "X" and cur[0]+1 == e_x and cur[1]+1 == e_y:
            ok = True
            break

if ok:
    print("YES")
else:
    print("NO")
