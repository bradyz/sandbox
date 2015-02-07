from random import randrange


class SinglyLinkedList:
    def __init__(self):
        self.front = None

    def add(self, val):
        tmp = Node(val)
        if not self.front:
            self.front = tmp
        else:
            it = self.front
            while it.head:
                it = it.head
            it.head = tmp

    def insert(self, index, val):
        it = self.front
        cur = 0
        if cur == index:
            tmp = Node(val)
            self.front = tmp
            tmp.head = it
            return cur
        prev = self.front
        it = it.head
        while it:
            if cur + 1 == index:
                tmp = Node(val)
                prev.head = tmp
                tmp.head = it
                return cur
            prev = it
            it = it.head
            cur += 1
        return -1

    def first(self):
        return self.front

    def last(self):
        it = self.front
        while it.head:
            it = it.head
        return it

    def index(self, val):
        it = self.front
        index = 0
        while it:
            if it.value == val:
                return index
            it = it.head
            index += 1
        return -1

    def size(self):
        length = 0
        it = self.front
        while it:
            length += 1
            it = it.head
        return length

    def find_mid(self):
        one = self.front
        two = self.front
        end = self.last()
        if not end:
            return None
        while two is not end:
            one = one.head
            two = two.head
            if two.head:
                two = two.head
        return one

    def remove_front(self):
        if self.front:
            self.front = self.front.head

    def to_array(self):
        tmp_list = []
        if self.front:
            it = self.front
            tmp_list = [it.value]
            while it.head:
                it = it.head
                tmp_list.append(it.value)
        return tmp_list


class Node:
    def __init__(self, val=None):
        self.value = val
        self.head = None

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    a = SinglyLinkedList()
    num = randrange(1, 10)

    for x in range(num):
        r = randrange(1, 10)
        a.add(r)

    print(a.to_array())
    print("Size: " + str(a.size()))
    print("Front: " + str(a.first()))
    print("Mid: " + str(a.find_mid()))
    print("Last: " + str(a.last()))
    a.remove_front()
    print("After Pop: " + str(a.to_array()))
    print("Size: " + str(a.size()))
    print("Index of 5: " + str(a.index(5)))
    a.add(10)
    print("Added 10: " + str(a.to_array()))
    a.insert(2, 8)
    print("Insert 8 at 2: " + str(a.to_array()))
