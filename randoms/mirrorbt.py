class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mirror_tree(r):
    if r:
        r.left, r.right = mirror_tree(r.right), mirror_tree(r.left)
    return r


def inorder(r):
    if not r:
        return

    inorder(r.left)
    print(r.val)
    inorder(r.right)

if __name__ == "__main__":
    print("Original:")
    root = Node(1, Node(3), Node(2, Node(5), Node(4)))
    inorder(root)

    print("\nMirror:")
    mirror = mirror_tree(root)
    inorder(mirror)
