def dfs(cur, lvl, found=False):
    if cur == x-1:
        found = True
    elif found and lvl == y:
        t.append(cur)

    if cur not in v:
        return

    for val in v[cur]:
        dfs(val, lvl+1, found)


def isPal(word):
    tmp = {}
    for val in word:
        if d[val] in tmp:
            tmp[d[val]] += 1
        else:
            tmp[d[val]] = 1
    odd = 0
    for val in tmp:
        if tmp[val] % 2 == 1:
            odd += 1
            if odd >= 2:
                return "No"
    return "Yes"


if __name__ == "__main__":
    n, m = map(int, input().split())
    v = {}
    c = list(map(int, input().split()))
    d = input()

    for i in range(n-1):
        if c[i]-1 not in v:
            v[c[i]-1] = [i+1]
        else:
            v[c[i]-1].append(i+1)

    for _ in range(m):
        x, y = map(int, input().split())
        t = []
        dfs(0, 1)
        print(isPal(t))
