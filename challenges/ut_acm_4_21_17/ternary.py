class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.middle = None

    def insert(self, to_add):
        if to_add < self.value and self.left is None:
            self.left = Node(to_add)
            return self.value
        elif to_add > self.value and self.right is None:
            self.right = Node(to_add)
            return self.value
        elif to_add == self.value and self.middle is None:
            self.middle = Node(to_add)
            return self.value

        if to_add < self.value:
            return self.left.insert(to_add)
        elif to_add > self.value:
            return self.right.insert(to_add)
        elif to_add == self.value:
            return self.middle.insert(to_add)


n, x = map(int, input().split())
root = Node(x)

for _ in range(n):
    print(root.insert(int(input())))
