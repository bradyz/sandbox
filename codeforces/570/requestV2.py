def populate(cur):
    if depth[cur] > y:
        return
    elif depth[cur] == y:
        words.append(cur)

    if cur not in parent:
        return

    for val in parent[cur]:
        populate(val)


def isPal():
    tmp = {}
    for val in words:
        if d[val] not in tmp:
            tmp[d[val]] = 1
        else:
            tmp[d[val]] += 1
    odds = 0
    for val in tmp:
        if tmp[val] % 2 == 1:
            odds += 1
            if odds >= 2:
                return "No"
    return "Yes"

if __name__ == "__main__":
    n, m = map(int, input().split())
    depth = [1 for _ in range(n)]
    parent = {}
    for i, val in enumerate(map(int, input().split())):
        depth[i+1] = depth[val-1] + 1
        if val-1 not in parent:
            parent[val-1] = [i+1]
        else:
            parent[val-1].append(i+1)
    d = input()
    for _ in range(m):
        x, y = map(int, input().split())
        words = []
        populate(x-1)
        print(isPal())
