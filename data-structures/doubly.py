class node:
    def __init__(self, val):
        self.val = val
        self.tail = None
        self.head = None

    def add(self, _node):
        cur = self

        while cur.head:
            cur = cur.head

        _node.tail = cur
        cur.head = _node

    def to_list(self):
        res = []
        cur = self

        while cur:
            res.append(cur)
            cur = cur.head

        return res

    def end(self):
        cur = self
        while cur.head:
            cur = cur.head
        return cur

    def size(self):
        cur = self
        count = 0
        while cur:
            count += 1
            cur = cur.head
        return count

    def reverse(self):
        cur = self
        end = self.end()

        for _ in range(self.size() / 2):
            print(map(str, self.to_list()))
            cur.val, end.val = end.val, cur.val
            cur = cur.head
            end = end.tail

    def __str__(self):
        return str(self.val)

if __name__ == "__main__":
    point = node(10)
    point.add(node(20))
    point.add(node(30))
    point.add(node(40))
    point.add(node(50))
    point.add(node(60))
    print(map(str, point.to_list()))

    for x in point.to_list():
        print(str(x.tail) + " " + str(x.val) + " " + str(x.head))
    point.reverse()
    print(map(str, point.to_list()))
    for x in point.to_list():
        print(str(x.tail) + " " + str(x.val) + " " + str(x.head))
    print(point.size())
