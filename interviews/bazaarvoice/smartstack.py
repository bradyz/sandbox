class SmartStack:
    def __init__(self):
        self.__init__stack = []
        self.min = []

    def stack_push(self, x):
        self.stack.append(x)
        if len(self.min) != 0:
            if x < self.stack_min():
                self.min.append(x)
            else:
                self.min.append(x)

    def stack_pop(self):
        x = self.stack.pop()
        if x == self.stack_min():
            self.min.pop()
        return x

    def stack_min(self):
        return self.min[-1]
