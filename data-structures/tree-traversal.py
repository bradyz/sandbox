class node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder(self):
        vis = [self]
        res = []
        cur = self

        while len(vis) > 0:
            if cur.left and cur.left not in res:
                cur = cur.left
                vis.append(cur)
            elif cur.right and cur.right not in res:
                cur = cur.right
                vis.append(cur)
            else:
                cur = vis.pop()
                res.append(cur)

        for x in res:
            print(x.val)

if __name__ == "__main__":
    root = node(20, node(8, node(4), node(12, node(10), node(14))), node(22))
    root.inorder()
