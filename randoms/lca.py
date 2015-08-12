class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def lca(r, a, b):
    def path(n, c):
        if not c:
            return None
        elif c.val == n:
            return [c.val]
        l = path(n, c.left)
        r = path(n, c.right)
        if l:
            return [c.val] + l
        elif r:
            return [c.val] + r
        else:
            return None

    return list(x for x, y in zip(path(a, r), path(b, r)) if x == y)[-1]


root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
print(lca(root, 7, 5))
