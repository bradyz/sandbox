class BST:
    def __init__(self):
        self.root = None

    def insert_val(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            cur = self.root
            it = True
            while it:
                if val < cur.value and cur.has_left():
                    cur = cur.left
                elif val >= cur.value and cur.has_right():
                    cur = cur.right
                else:
                    it = False
            if val < cur.value:
                cur.left = Node(val)
            else:
                cur.right = Node(val)

    def has_val(self, val):
        return True

    def root(self):
        return self.root

    def pre_order(self, node=None):
        if node:
            yield node.value
            for x in self.pre_order(node.left):
                yield x
            for x in self.pre_order(node.right):
                yield x

    def in_order(self, node=None):
        if node:
            for x in self.in_order(node.left):
                yield x
            yield node.value
            for x in self.in_order(node.right):
                yield x

    def post_order(self):
        return 0


class Node:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def __str__(self):
        return str(self.value)

if __name__ == "__main__":
    bst = BST()
    bst.insert_val(2)
    bst.insert_val(1)
    bst.insert_val(3)

    root = bst.root

    print("In_order: ")
    ino = bst.in_order(root)
    for x in ino:
        print(x)

    print("Pre_order: ")
    preo = bst.pre_order(root)
    for x in preo:
        print(x)
