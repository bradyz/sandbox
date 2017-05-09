from collections import deque


def solve(tree, need, parent, leaves):
    result = 0

    queue = deque()
    for u in leaves:
        queue.appendleft(u)

    while len(queue) > 0:
        u = queue.popleft()

        if u in need:
            need.remove(u)

            if parent[u] in need:
                need.remove(parent[u])
            if parent[u] != 0 and parent[parent[u]] in need:
                need.remove(parent[parent[u]])

            for v in tree.get(parent[u], list()):
                if v in need:
                    need.remove(v)

            result += 1

        if u in parent:
            queue.appendleft(parent[u])

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

    print(solve(tree, need, parent, leaves))
