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
            cur = s.pop()
            if cur:
                s.append(cur.right)
                s.append(cur)
                s.append(cur.left)
            else:
                if len(s) > 0:
                    res.append(s.pop())

        return res

    def preorder(self):
        s = [self]
        res = []

        while len(s) > 0:
            cur = s.pop()
            if cur:
                res.append(cur)
                s.append(cur.right)
                s.append(cur.left)

        return res

    def postorder(self):
        s = [self]
        res = []

        while len(s) > 0:
            cur = s.pop()
            if cur:
                if cur not in res:
                    s.append(cur)
                    s.append(None)
                if cur.right not in res:
                    s.append(cur.right)
                if cur.left not in res:
                    s.append(cur.left)
            else:
                if len(s) > 0 and s[-1]:
                    res.append(s.pop())
        return res

    def level_order(self):
        q = Queue()
        res = []
        q.put(self)

        while not q.empty():
            cur = q.get()
            if cur:
                res.append(cur)
                q.put(cur.left)
                q.put(cur.right)

        return res

    def __str__(self):
        return str(self.val)

    def __int__(self):
        return self.val


if __name__ == "__main__":
    root = node(20, node(8, node(4), node(12, node(10), node(14))), node(22))

    a = root.inorder()
    print("In Order => [4, 8, 10, 12, 14, 20, 22]")
    print(map(int, a))
    print("")

    b = root.level_order()
    print("Level Order => \t[20, 8, 22, 4, 12, 10, 14]")
    print(map(int, b))
    print("")

    c = root.preorder()
    print("Pre Order => [20, 8, 4, 12, 10, 14, 22]")
    print(map(int, c))
    print("")

    d = root.postorder()
    print("Post Order: [4, 10, 14, 12, 8, 22, 20]")
    print(map(int, d))
    print("")
