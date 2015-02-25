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

    def insert(self, d):
        if not self.data:
            self = Node(d)
        if d < self.data:
            if self.left:
                self.left.insert(d)
            else:
                self.left = Node(d)
        else:
            if self.right:
                self.right.insert(d)
            else:
                self.right = Node(d)

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
    root = Node(3)
    root.insert(2)
    root.insert(1)

    res = ""
    for x in root.inorder():
        res += str(x) + " "
    print(res)

    print(root.is_bst())
