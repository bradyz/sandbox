from queue import Queue


class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = []

    def add(self, other):
        self.children.append(other)

    def __str__(self):
        return "Val: " + str(self.val) + " Children: " + \
            " ".join(map(str, (v.val for v in self.children)))


def printLevelOrder(r):
    s = Queue()
    s.put((r, 0))
    p_l = -1
    level = []

    while not s.empty():
        c, l = s.get()
        for v in c.children:
            s.put((v, l+1))
        if l > p_l:
            print(" ".join(map(str, (v.val for v in level))))
            level = []
        level.append(c)
        p_l = l

    if level:
        print(" ".join(map(str, (v.val for v in level))))


if __name__ == "__main__":
    n = int(input())
    d = dict()

    for _ in range(n):
        u, v = map(int, input().split())
        if u not in d:
            d[u] = Node(u)
        if v not in d:
            d[v] = Node(v)
        d[u].add(d[v])

    print("\n".join(map(str, (v for v in d.values()))))
    printLevelOrder(d[1])
