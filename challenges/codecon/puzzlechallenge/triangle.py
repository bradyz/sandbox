import sys
g = [list(line.strip()) for line in sys.stdin]
n = len(g)
m = len(g[0])
r = 0


for i in range(n):
    for j in range(m):
        t = g[i][j]
        k = 0
        while i+k < n and j+k < m:
            if g[i+k][j+k] != t:
                break
            k += 1
        l = 0
        while i-l >= 0 and j+l < m:
            if g[i-l][j+l] != t:
                break
            l += 1
        if k > 1:
            for y in range(1, k+1):
                x = 0
                while x < y:
                    if g[i+y-1][j+x] != t or g[i+y-1][j-x+y-1] != t:
                        break
                    x += 1
                if x == y:
                    r = max(r, (y+1)*(y)//2)
        if k > 1:
            for y in range(1, k+1):
                x = 0
                while x < y:
                    if g[i][j+x] != t or g[i+y-1-x][j+y-1] != t:
                        break
                    x += 1
                if x == y:
                    r = max(r, (y+1)*(y)//2)
        if l > 1:
            for y in range(1, l+1):
                x = 0
                while x < y:
                    if g[i-x][j] != t or g[i-y+1][j+x] != t:
                        break
                    x += 1
                if x == y:
                    r = max(r, (y+1)*(y)//2)
        if l > 1:
            for y in range(1, l+1):
                x = 0
                while x < y:
                    if g[i][j+x] != t or g[i-x][j+y-1] != t:
                        break
                    x += 1
                if x == y:
                    r = max(r, (y+1)*(y)//2)

print(r)
