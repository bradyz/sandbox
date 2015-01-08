class Stack:
    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, index):
        return self.stack[index]

    def __str__(self):
        return str(self.stack)


class QueueStack:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def q(self, el):
        self.s1.push(el)

    def dq(self):
        if len(self.s2) > 0:
            return self.s2.pop()
        for x in range(len(self.s1)):
            self.s2.push(self.s1.pop())

        return self.s2.pop()

    def __str__(self):
        tmp = []

        for x in range(len(self.s2) - 1, -1, -1):
            tmp.append(self.s2[x])

        for x in range(0, len(self.s1)):
            tmp.append(self.s1[x])

        return str(tmp)

if __name__ == "__main__":
    my_qs = QueueStack()
    my_qs.q(1)
    my_qs.q(2)
    my_qs.q(3)
    print(str(my_qs))
    print(str(my_qs.dq()))
    print(str(my_qs))
