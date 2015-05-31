class node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_bst(self):
        if self.right and self.left:
            if self.left < self and self < self.right:
                return self.right.is_bst() and self.left.is_bst()
            else:
                return False
        elif self.right:
            return self.right > self and self.right.is_bst()
        elif self.left:
            return self.left < self and self.left.is_bst()
        else:
            return True

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

if __name__ == "__main__":
    root = node(20, node(8, node(4), node(12, node(10), node(14))), node(22))
    print(root.is_bst())
    root = node(20, node(8, node(4), node(12, node(14), node(10))), node(22))
    print(root.is_bst())
