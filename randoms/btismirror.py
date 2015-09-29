class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_mirror(root):
    # print(" ".join(map(str, left_dfs(root.left))))

    print(not any(x != y for x, y in zip(right_dfs(root.right),
                                         left_dfs(root.left))))


def right_dfs(root):
    if not root:
        yield None
    else:
        yield root.val
        for val in right_dfs(root.right):
            yield val
        for val in right_dfs(root.left):
            yield val


def left_dfs(root):
    if not root:
        yield 0
    else:
        yield root.val
        for val in right_dfs(root.left):
            yield val
        for val in right_dfs(root.right):
            yield val

if __name__ == "__main__":
    mirror = Node(1, Node(2, None, Node(3)), Node(2, Node(3)))
    is_mirror(mirror)

    notmirror = Node(1, Node(2, Node(3)), Node(2, Node(3)))
    is_mirror(notmirror)
