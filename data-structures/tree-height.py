class AVL:
    def __init__(self, root=None, vals=None):
        self.root = root

        if self.root:
            for val in vals:
                self.root.add(val)

    def add(self, node):
        pass


class node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def height(self):
        if self.right and self.left:
            return max(self.right.height()+1, self.left.height()+1)
        elif self.right:
            return self.right.height()+1
        elif self.left:
            return self.left.height()+1
        else:
            return 1

    def __gt__(self, other):
        return self.val > other.val

    def __lt__(self, other):
        return self.val < other.val

    def __ge__(self, other):
        return self.val > other.val or self == other

    def __le__(self, other):
        return self.val < other.val or self == other

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return not self == other


if __name__ == "__main__":
    avl = AVL()
    a = node(1)
    b = node(1)
