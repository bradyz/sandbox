from Queue import Queue


class node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder(self):
        s = [self]
        res = []

        while len(s) > 0:
            print(map(str, res))
            cur = s[-1]
            if cur.left and cur.left not in res:
                s.append(cur.left)
            elif cur.right and cur.right not in res:
                res.append(s.pop())
                s.append(cur.right)
            else:
                res.append(s.pop())

        return res

    def preorder(self):
        s = [self]
        res = []

        while len(s) > 0:
            print(map(str, res))
            cur = s.pop()
            res.append(cur)
            if cur.right:
                s.append(cur.right)
            if cur.left:
                s.append(cur.left)

        return res

    def level_order(self):
        q = Queue()
        res = []
        q.put(self)

        while not q.empty():
            print(map(str, res))
            cur = q.get()
            if cur:
                res.append(cur)
                q.put(cur.left)
                q.put(cur.right)

        return res

    def __str__(self):
        return str(self.val)


if __name__ == "__main__":
    root = node(20, node(8, node(4), node(12, node(10), node(14))), node(22))
    i = root.inorder()
    print(map(str, i))
    l = root.level_order()
    print(map(str, l))
    p = root.preorder()
    print(map(str, p))
