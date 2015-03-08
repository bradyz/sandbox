class node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return not (self == other)

    def path(self, other):
        cur = self
        path = [self]
        while cur != other:
            if other < cur:
                cur = cur.left
            else:
                cur = cur.right
            path.append(cur)
        return path

    def lcm(self, a, b):
        a_trail = self.path(a)
        b_trail = self.path(b)
        for i in range(min(len(a_trail), len(b_trail))):
            if a_trail[i] != b_trail[i]:
                return a_trail[i-1]
        return 0

    def inorder(self):
        vis = []
        cur = self
        stack = [cur]

        while len(stack) > 0:
            if cur.left and cur.left not in vis:
                stack.append(cur.left)
                cur = cur.left
            elif cur.right and cur.right not in vis:
                stack.append(cur.right)
                cur = cur.right
            else:
                cur = stack.pop()
                vis.append(cur)

        return vis

    def preorder(self):
        vis = []
        cur = self
        stack = [cur]

        while len(stack) > 0:
            cur = stack.pop()
            vis.append(cur)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return vis

    def postorder(self):
        vis = []
        cur = self
        stack = [cur]

        while len(stack) > 0:
            cur = stack[-1]
            if cur.left and cur.left not in vis:
                stack.append(cur.left)
            elif cur.right and cur.right not in vis:
                stack.append(cur.right)
            else:
                cur = stack.pop()
                vis.append(cur)

        return vis

    def __str__(self):
        return str(self.val)


if __name__ == "__main__":
    root = node(20, node(8, node(4), node(12, node(10), node(14))), node(22))
    a = root.postorder()
    print(root.lcm(node(10), node(4)))
