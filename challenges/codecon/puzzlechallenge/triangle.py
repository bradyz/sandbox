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
        if k > 0:
            x = 0
            while x < k:
                if g[i+k-1][j+x] != t or g[i+k-1][j-x+k-1] != t:
                    break
                x += 1
            if x == k:
                r = max(r, (k+1)*(k)//2)
        if k > 0:
            x = 0
            while x < k:
                if g[i][j+x] != t or g[i+k-1-x][j+k-1] != t:
                    break
                x += 1
            if x == k:
                r = max(r, (k+1)*(k)//2)
        if l > 0:
            x = 0
            while x < l:
                if g[i-x][j] != t or g[i-l+1][j+x] != t:
                    break
                x += 1
            if x == l:
                r = max(r, (l+1)*(l)//2)
        if l > 0:
            x = 0
            while x < l:
                if g[i][j+x] != t or g[i-x][j+l-1] != t:
                    break
                x += 1
            if x == l:
                r = max(r, (l+1)*(l)//2)

print(r)
