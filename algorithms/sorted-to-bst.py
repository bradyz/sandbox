class node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add(self, a_node):
        if a_node.val < self.val:
            if self.left:
                self.left.add(a_node)
            else:
                self.left = a_node
        else:
            if self.right:
                self.right.add(a_node)
            else:
                self.right = a_node

    def inorder(self):
        cur = self
        s = [self]
        res = []

        while len(s) > 0:
            cur = s.pop()
            if cur:
                s.append(cur.right)
                s.append(cur)
                s.append(cur.left)
            else:
                if s:
                    res.append(s.pop())

        return res

    def __str__(self):
        return str(self.val)


def to_bst(al):
    l = len(al)
    mid = l//2
    root = node(al[mid])
    if len(al[:mid]) > 0:
        root.add(to_bst(al[:mid]))
    if len(al[mid+1:]) > 0:
        root.add(to_bst(al[mid+1:]))
    return root

if __name__ == "__main__":
    a_list = [1, 2, 3, 4, 5, 6, 7]
    a_bst = to_bst(a_list)
    b = a_bst.inorder()
    print(a_list)
    for x in b:
        print(x.left, x.val, x.right)
