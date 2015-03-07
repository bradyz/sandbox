# level order traversal of binary tree
# [15, 10, 9, 8, 9, 6, 3, 4, 2]
# node at index k has children 2k+1, 2k+2
# node at index k has parent at (k-1)/2


class heap:
    def __init__(self, items=None):
        if items:
            self.items = items
        else:
            self.items = []

    def insert(self, val):
        self.items.append(val)
        self.siftup()

    def delete(self):
        if len(self.items) == 0:
            return None
        elif len(self.items) == 1:
            return self.items.pop()
        else:
            tmp = self.items[0]
            self.items[0] = self.items.pop()
            self.siftdown()
            return tmp

        return 0

    def siftup(self):
        k = len(self.items) - 1
        while k > 0:
            p = (k-1)/2
            cur = self.items[k]
            par = self.items[p]

            if cur > par:
                self.items[k], self.items[p] = par, cur
                cur = par
            else:
                break

    def siftdown(self):
        k = 0
        l = 2*k+1
        while l < len(self.items):
            m = l
            r = l+1
            if r < len(self.items):
                if self.items[r] > self.items[l]:
                    m = r
            if self.items[k] < self.items[m]:
                self.items[k], self.items[m] = self.items[m], self.items[k]
                k = m
                l = 2*k+1
            else:
                break

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    a = [15, 10, 9, 8, 9, 6, 3, 4, 2]
    h = heap(a)
    print(h)
    while h.size() > 0:
        print(h.delete())
