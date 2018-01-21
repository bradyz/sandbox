from collections import defaultdict, deque


def solve(tree, num_knights):
    root = find_root(tree)

    parent = dict()
    parent[root] = None

    queue = deque()
    queue.append(root)

    levels = list()

    while queue:
        new_queue = deque()

        current_level = list()

        while queue:
            u = queue.popleft()

            current_level.append(u)

            for v in tree[u]:
                new_queue.append(v)
                parent[v] = u

        levels.append(current_level)
        queue = new_queue

    changes = 0

    for i in range(len(levels)-2, -1, -1):
        for u in levels[i]:
            can_overtake = list()

            for v in tree[u]:
                if num_knights[v] >= num_knights[u] + 3:
                    can_overtake.append((-num_knights[v], v))

            can_overtake.sort()

            if can_overtake:
                changes += 1

                v = can_overtake[0][1]

                tree[u], tree[v] = tree[v], tree[u]
                tree[v].remove(v)
                tree[v].add(u)

                if parent[u]:
                    tree[parent[u]].add(v)
                    tree[parent[u]].remove(u)

    return changes, levels


def find_root(tree):
    root = set(tree.keys())

    for _, banner in tree.items():
        for person in banner:
            if person in root:
                root.remove(person)

    return root.pop()


n = int(input())

tree = defaultdict(set)
num_knights = dict()

for _ in range(n):
    line = input().split()

    name = line[0]
    knights = int(line[1])
    banner = set(line[3:])

    num_knights[name] = knights
    tree[name] = banner


changes, levels = solve(tree, num_knights)
_, levels = solve(tree, num_knights)

for level in levels:
    print(' '.join(map(str, sorted(level))))
