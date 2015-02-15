# Min Stack Description:
# implement a stack that allows a function min() that
# returns the minimum value in O(1)


class Minstack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def spush(self, x):
        self.s1.append(x)
        if len(self.s2) == 0 or x <= self.stack_min():
            self.s2.append(x)

    def spop(self):
        x = self.s1.pop()
        if x == self.stack_min():
            self.s2.pop()
        return x

    def smin(self):
        return self.s2[-1]
