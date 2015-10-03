from sys import maxsize as MAXINT
from queue import PriorityQueue


class Node:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, rhs):
        return self.b < rhs.b

    def __eq__(self, rhs):
        return self.b == rhs.b


def solve():
    b = dict()
    x = dict()
    q = PriorityQueue()

    for i in range(1, 10):
        q.put((Node(int(i * str(d)), i)))
        b[i] = b.get(i, []) + []

    while not q.empty():
        c = q.get_nowait()
        if c.b > 9 or (c.b >= b.get(c.a, MAXINT)):
            continue
        if c.a == n:
            return c.b

        b[c.a] = c.b

        for i in range(1, 10):
            y = int(i*str(d))
            q.put_nowait(Node(c.a + y, c.b+i))
            q.put_nowait(Node(c.a - y, c.b+i))
            q.put_nowait(Node(c.a * y, c.b+i))
            q.put_nowait(Node(c.a // y, c.b+i))


for _ in range(int(input())):
    d, n = map(int, input().split())
    print(solve())
