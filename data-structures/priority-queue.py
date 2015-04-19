class NaivePQ:
    def __init__(self, l=None):
        self.top = None
        self.l = l

    def pop(self):
        min_tmp = max(self.l)
        min_i = 0

        for i, val in enumerate(self.l):
            if val < min_tmp:
                min_tmp = val
                min_i = i

        self.l = self.l[:min_i] + self.l[min_i+1:]
        return min_tmp

    def push(self, val):
        self.l.append(val)

    def __str__(self):
        return str(self.l)

if __name__ == "__main__":
    a = NaivePQ([5, 3, 1, 2, 4, 1])
    print(a)
    print(a.pop())
    print(a)
