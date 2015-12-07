def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if par[y] < par[x]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x


def find(i):
    if par[i] < 0:
        return i
    par[i] = find(par[i])
    return par[i]

if __name__ == "__main__":
    N, I = map(int, input().split())
    par = [-1 for u in range(N)]
    for _ in range(I):
        u, v = map(int, input().split())
        union(u, v)
    cou = dict()
    for i in range(N):
        cou[find(i)] = cou.get(find(i), 0) + 1
    cou = [0] + [val for val in cou.values()]
    res = 0
    for i in range(1, len(cou)):
        res += cou[i] * cou[i-1]
        cou[i] += cou[i-1]
    print(res)
