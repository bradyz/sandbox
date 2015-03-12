class node:
    def __init__(self, val, head=None):
        self.val = val
        self.head = head

    def __str__(self):
        return str(self.val)


class singly:
    def __init__(self, front):
        self.front = front

    def reverse(self):
        prev = self.front
        cur = prev.head
        prev.head = None
        while cur:
            tmp = cur.head
            cur.head = prev
            prev = cur
            cur = tmp
        self.front = prev

    def __str__(self):
        res = []
        tmp = self.front

        while tmp:
            res.append(tmp)
            tmp = tmp.head

        return str(map(str, res))

if __name__ == "__main__":
    a = singly(node(1, node(2, node(3, node(4)))))
    print(a)
    a.reverse()
    print(a)
