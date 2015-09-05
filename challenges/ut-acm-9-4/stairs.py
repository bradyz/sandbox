def dfs(c=0):
    if c > n:
        return 0
    elif c == n:
        return 1

    return sum(dfs(c+u) for u in d)

for _ in range(int(input())):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))

    print(dfs())
