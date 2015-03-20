class node:
    def __init__(self, key=None, val=None, head=None, tail=None):
        self.key = key
        self.val = val
        self.head = head
        self.tail = tail

    def __str__(self):
        return str(self.val)


class LRU:
    def __init__(self, cap=5):
        self.cap = cap
        self.first = None
        self.last = None
        self.m = {}
        print("Creating LRU of Capacity: " + str(self.cap))

    def assign(self, key, val):
        print("Assigned Key: "+str(key)+" Val: "+str(val))
        if key in self.m:
            self.m[key].val = val
            self.promote(key)
        else:
            if len(self.m.keys()) >= self.cap:
                self.evict()
            if not self.first:
                self.first = node(key, val, head=self.last)
                self.m[key] = self.first
            elif not self.last:
                self.last = node(key, val, tail=self.first)
                self.first.head = self.last
                self.m[key] = self.last
            else:
                self.last.head = node(key, val, tail=self.last)
                self.last = self.last.head
                self.m[key] = self.last
        print(str(self))

    def get(self, key):
        if key in self.m:
            self.promote(key)
            return self.m[key].val
        return -1

    def evict(self):
        print("Reached capacity! Evicting...")
        tmp = self.first.key
        self.first = self.first.head
        self.first.tail = None
        self.m.pop(tmp)

    def promote(self, key):
        if self.m[key] == self.last:
            return
        if self.m[key] == self.first:
            self.first = self.first.head
        if self.m[key].tail:
            self.m[key].tail.head = self.m[key].head
        if self.m[key].head:
            self.m[key].head.tail = self.m[key].tail
        self.m[key].head = None
        self.m[key].tail = self.last
        self.last.head = self.m[key]
        self.last = self.m[key]

    def __str__(self):
        cur = self.first
        res = []
        while cur:
            res.append(cur)
            cur = cur.head
        return str(map(str, res))


if __name__ == "__main__":
    a = LRU(4)
    for i in range(1, 6):
        a.assign(i, i)

    print("Get 2 => " + str(a.get(2)))  # get least recent node
    print(a)

    print("Get 2 => " + str(a.get(2)))  # get most recent node
    print(a)
    for i in range(5, 10):
        a.assign(i, i)
        if i % 2:
            print("Get 2 => " + str(a.get(2)))
            print(a)
