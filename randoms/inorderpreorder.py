class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def inorder(r):
    if r:
        for v in inorder(r.left):
            yield v
        yield r.val
        for v in inorder(r.right):
            yield v


def preorder(r):
    if r:
        yield r.val
        for v in preorder(r.left):
            yield v
        for v in preorder(r.right):
            yield v


def solve(n, i, p):
    def reconstruct(io=i, po=p):
        if not po or not io:
            return None

        r = t[po[0]]
        r_i = io.index(r.val)
        r.left = reconstruct(io[:r_i], po[1:r_i+1])
        r.right = reconstruct(io[r_i+1:], po[r_i+1:])

        return r

    t = {x: Node(x) for x in range(1, n+1)}
    reconstruct()

    return t

if __name__ == "__main__":
    n, m = map(int, input().split())
    t = {i: Node(i) for i in range(1, m+1)}

    for _ in range(n):
        is_left, u, v = map(int, input().split())
        if is_left:
            t[u].left = t[v]
        else:
            t[u].right = t[v]

    new_tree = solve(m, list(inorder(t[1])), list(preorder(t[1])))
