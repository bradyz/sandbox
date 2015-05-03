# 500B: New Year Permutation
# Start Time: 11:46 p.m. 5-2-15
# End Time: 11:46 p.m. 5-2-15


def dfs(x):
    p.append(x)
    for i in range(n):
        if g[x][i] and not u[i]:
            u[i] = True
            dfs(i)

if __name__ == "__main__":
    n = int(input())
    v = list(map(int, input().split()))
    g = [[i == "1" for i in input()] for j in range(n)]

    u = [False for _ in range(n)]

    for i in range(n):
        if not u[i]:
            p = []
            dfs(i)
            val = [v[i] for i in p]
            p.sort()
            val.sort()
            print(p, val)
            for x, y in enumerate(p):
                v[y] = val[x]
print(v)
