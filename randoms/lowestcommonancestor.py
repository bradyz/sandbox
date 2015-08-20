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


def lcaV2(r, a, b):
    if not r:
        return None
    elif r.val == a or r.val == b:
        return r.val
    left = lcaV2(r.left, a, b)
    right = lcaV2(r.right, a, b)
    if left and right:
        return r.val
    elif left:
        return left
    elif right:
        return right


root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

print(lca(root, 6, 7))
print(lcaV2(root, 6, 7))
