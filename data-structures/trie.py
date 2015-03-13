# Trie aka Prefix Tree
# _r is root
# _c is children
# _l is letter


class Trie:
    def __init__(self, words=None):
        self._r = Node("")
        self.words = set()
        if words:
            self.words = set(words)
            for w in self.words:
                self.insert(w)

    # inserts word w at node n
    def insert(self, w, n=None):
        if not n:
            n = self._r
        if len(w) > 0:
            if not n.child(w[:1]):
                n.add(Node(w[:1]))
                self.insert(w[1:], n.child(w[:1]))
            else:
                self.insert(w[1:], n.child(w[:1]))

    def auto(self, w):
        cur = self._r
        i = 0
        while i < len(w):
            if cur.child(w[i]):
                cur = cur.child(w[i])
                i += 1
            else:
                break

        res = []
        for x in cur.all():
            if (w[:i] + x) in self.words:
                res.append(w[:i] + x)
        return res

    def remove(self, word):
        return 0

    def all(self):
        return self._r.all()

    def __iter__(self):
        return self._r.chars()

    def __str__(self):
        return str(self._r.chars())


class Node:
    def __init__(self, l=None):
        self._c = []
        self._l = l

    def chars(self):
        return self._c

    def add(self, l):
        if l not in self._c:
            self._c.append(l)

    def child(self, l):
        for child in self.chars():
            if child._l == l:
                return child
        return None

    def all(self):
        cur = self
        tmp = ""
        res = []
        stack = [cur]
        wstack = [tmp]
        while len(stack) > 0:
            for x in cur.chars():
                stack.append(x)
                wstack.append(tmp+x._l)
                res.append(tmp+x._l)
            if len(stack) > 0:
                cur = stack.pop()
                tmp = wstack.pop()
        return res

    def __eq__(self, other):
        return self._l == other._l

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self._l)

    def __iter__(self):
        return self._c

if __name__ == "__main__":
    words = ["cat", "cow", "calf", "camry"]
    a = Trie(words)
    print(a.auto("ca"))
