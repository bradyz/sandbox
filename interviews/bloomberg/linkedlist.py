class SinglyLinkedList:
    def __init__(self):
        self.front = None

    def add(self, value):
        tmp = Node(value)
        if not self.front:
            self.front = tmp
        else:
            it = self.front
            while it.next:
                it = it.next
            it.next = tmp

    def getFirst(self):
        return 0

    def getLast(self):
        return 0

    def indexOf(self):
        return 0

    def side(self):
        return 0

    def removeFirst(self):
        return 0

    def toArray(self):
        tmp_list = [self.front.value]
        if self.front:
            it = self.front
            while it.next:
                it = it.next
                tmp_list.append(it.value)

        return tmp_list


class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None

    def __str__(self):
        return str(self.value)

a = SinglyLinkedList()
a.add(10)
a.add(1)
print(a.toArray())
