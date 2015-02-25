class Node:
    def __init__(self, d=None):
        self.data = d
        self.left = None
        self.right = None

    def inorder(self):
        if self:
            if self.left:
                for l in self.left.inorder():
                    yield l
            yield self
            if self.right:
                for r in self.right.inorder():
                    yield r

    def is_bst(self):
        prev = None
        for val in self.inorder():
            if not prev:
                prev = val.data
            else:
                if val.data < prev:
                    return False
                prev = val.data
        return True

    def __str__(self):
        return str(self.data)

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    res = ""
    for x in root.inorder():
        res += str(x) + " "
    print(res)

    print(root.is_bst())
