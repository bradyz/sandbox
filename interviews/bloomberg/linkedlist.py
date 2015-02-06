class SinglyLinkedList:
    def __init__(self):
        self.front = None
        self.nodelist = []

    def insert(self, node):
        if not self.front:
            self.front = node
        else:
            tmp = self.front
            while tmp.next:
                tmp = tmp.next
            tmp.next = node
        self.nodelist.append(node)


class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None

    def __str__(self):
        return str(self.value)

a = SinglyLinkedList()
b = Node(10)
a.insert(b)
print(a.nodelist)
