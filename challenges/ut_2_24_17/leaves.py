class Node:
    def __init__(self, value, level, column):
        self.value = value
        self.level = level
        self.column = column
        self.left = None
        self.right = None

    def insert(self, value, level):
        if value < self.value:
            if self.left is None:
                self.left = Node(value, level+1, self.column - 1)
            else:
                self.left.insert(value, level+1)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value, level+1, self.column + 1)
            else:
                self.right.insert(value, level+1)

    def get_all(self, all_values):
        all_values.append((self.value, self.column, self.level))
        if self.left is not None:
            self.left.get_all(all_values)
        if self.right is not None:
            self.right.get_all(all_values)


for _ in range(int(input())):
    n = int(input())
    values = list(map(int, input().split()))

    root = Node(values[0], 0, 0)

    for i in range(1, n):
        root.insert(values[i], 0)

    order = list()
    root.get_all(order)

    order.sort(key=lambda x: (x[1], x[2], x[0]))
    order = [z[0] for z in order]

    print(" ".join(map(str, order)))
