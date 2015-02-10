import sys


class BST:
    def __init__(self):
        self.root = Node()

    def insert_val(self, val):
        if not self.root.value:
            self.root = Node(val)
        else:
            cur = self.root
            while cur:
                if val < cur.value:
                    cur = cur.left
                else:
                    cur = cur.right
            cur = Node(val)

    def has_val(self, val):
        return True

    def root(self):
        return self.root

    def pre_order(self):
        return 0

    def in_order(self):
        return 0

    def post_order(self):
        return 0


class Node:
    def __init__(self, val=None):
        self.value = val
        self.parent = None
        self.left = None
        self.right = None

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        arr = [int(x) for x in line.split()]
        bst = BST()
        sorted_arr = sorted(arr)
        for x in sorted_arr:
            bst.insert_val(x)
