class node:
    def __init__(self, val, head=None):
        self.val = val
        self.head = head

    def __str__(self):
        return str(self.val)


class singly:
    def __init__(self, front=None):
        self.front = front

    def add(self, n):
        end = self.last()
        if not end:
            self.front = n
        else:
            end.head = n

    def last(self):
        tmp = self.front

        if not tmp:
            return None

        while tmp.head:
            tmp = tmp.head

        return tmp

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

    def reverse_words(self):
        prev = self.front
        cur = prev.head

        while cur:
            while cur.val != " ":
                tmp = cur.head
                cur.head = prev
                prev = cur
                cur = tmp
        return 0

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
    b = singly()
    b.add(node("a"))
    b.add(node("b"))
    b.add(node("c"))
    b.add(node(" "))
    b.add(node("d"))
    b.add(node("e"))
    print(b)
