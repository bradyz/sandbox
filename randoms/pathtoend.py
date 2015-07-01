c = [1, 2, 4, 0, 0, 0, 1]


def walk(a):
    i = 0
    j = a[0]
    while j >= 0 and i < len(a):
        if a[i] > j-1:
            j = a[i]
        else:
            j -= 1
        i += 1
    if i == len(a):
        print("YES")
    else:
        print("NO")


def dfsway(a):
    def dfs(i, v):
        if i >= len(a):
            return True
        elif v[i]:
            return False
        else:
            v[i] = True
            e = False
            for j in range(a[i]+1):
                e |= dfs(i+a[j], v)
            return e

    vis = [False for _ in a]
    print(dfs(0, vis))

walk(c)
dfsway(c)
