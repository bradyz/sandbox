class Node:
    def __init__(self, v=None, l=None, r=None):
        self.val = v
        self.l = l
        self.r = r

    def inorder_succ(self, val):
        parent_stack = []
        cur = self
        while cur.val != val:
            parent_stack.append(cur.val)
            if val > cur.val:
                cur = cur.r
            else:
                cur = cur.l
        print(val, parent_stack)
        while len(parent_stack) > 0:
            tmp = parent_stack.pop()
            if tmp > val:
                return tmp
        return 0

if __name__ == "__main__":
    root = Node(20, Node(8, Node(4), Node(12, Node(10), Node(14))), Node(22))
    print(root.inorder_succ(8))
    print(root.inorder_succ(10))
    print(root.inorder_succ(14))
