class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def beginning(self):
        if self.left:
            return self.left.beginning()
        return self

    def __str__(self):
        r = "Left: "
        if self.left:
            r += str(self.left.val)
        else:
            r += "0"
        r += "\tVal: " + str(self.val) + "\tRight: "
        if self.right:
            r += str(self.right.val)
        else:
            r += "0"
        return r


def solve(r):
    def bsttodoublylinked(root):
        nonlocal prev

        if not root:
            return

        bsttodoublylinked(root.left)

        if prev:
            prev.right = root
        root.left = prev
        prev = root

        bsttodoublylinked(root.right)

        return root

    prev = None
    return bsttodoublylinked(r)


def printdoubly(b):
    if b:
        yield b

        for v in printdoubly(b.right):
            yield v


if __name__ == "__main__":
    bst = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    a = solve(bst)

    b = a.beginning()

    for v in printdoubly(b):
        print(v)
