import sys


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBST(r, minVal=-sys.maxsize, maxVal=sys.maxsize):
    if not r:
        return True
    elif r.val < minVal or r.val > maxVal:
        return False
    return isBST(r.left, minVal, r.val) and isBST(r.right, r.val, maxVal)

isYes = Node(4, Node(2, Node(1), Node(3)), Node(5))
isNot = Node(3, Node(2, Node(1), Node(4)), Node(5))

print(isBST(isYes))
print(isBST(isNot))
