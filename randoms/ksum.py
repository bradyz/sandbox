c = list(map(int, input().split()))
k = int(input())


def dfs(u, r):
    if r == k:
        return True
    elif r > k:
        return False
    return any(dfs(i, c[i]+r) for i in range(u+1, len(c)))

print(c, k)
print(any(dfs(i, 0) for i in range(len(c))))
