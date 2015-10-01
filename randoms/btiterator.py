class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BT:
    class BT_iterator:
        def __init__(self, root):
            self.gen = self.inorder(root)

        def inorder(self, cur):
            if cur:
                for node in self.inorder(cur.left):
                    yield node
                yield cur
                for node in self.inorder(cur.right):
                    yield node

        def __iter__(self):
            return self

        def __next__(self):
            return next(self.gen)

    def __init__(self, node=None):
        self.root = node

    def __iter__(self):
        return BT.BT_iterator(self.root)


if __name__ == "__main__":
    fake_bst = BT(Node(2,
                       Node(1), Node(3)))

    for val in fake_bst:
        print(val.val)
