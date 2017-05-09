from heapq import heappush, heappop


def solve(tree, need, parent, leaves, level):
    result = 0

    queue = list()
    for u in parent:
        heappush(queue, (-level[u], u))

    while len(queue) > 0:
        _, u = heappop(queue)

        if u in need:
            if parent[u] in need:
                need.remove(parent[u])
            if parent[u] != 0 and parent[parent[u]] in need:
                need.remove(parent[parent[u]])

            for v in tree.get(parent[u], list()):
                if v in need:
                    need.remove(v)

            result += 1

    return result


if __name__ == '__main__':
    tree = dict()
    parent = dict()
    need = set()
    leaves = set()

    for i in range(1, int(input())):
        u, s = map(int, input().split())
        if u not in tree:
            tree[u] = list()
        tree[u].append(i)
        parent[i] = u
        if s == 0:
            need.add(i)

    for u in parent:
        if u not in tree:
            leaves.add(u)

    level = {0: 0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in tree.get(u, list()):
            level[v] = level[u] + 1
            stack.append(v)

    print(solve(tree, need, parent, leaves, level))
