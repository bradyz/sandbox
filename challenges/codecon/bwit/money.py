n = int(input())
c = [int(input()) for _ in range(n)]


def move(m, i, j):
    if i > j:
        return 0
    if m:
        return max(c[i]+move(False, i+1, j), c[j]+move(False, i, j-1))
    else:
        if c[i] > c[j]:
            return move(True, i+1, j)
        else:
            return move(True, i, j-1)

r = move(True, 0, n-1)

print(r)
