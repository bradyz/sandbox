import queue


class q():
    def __init__(self, l=None):
        self._q = queue.Queue()
        for i in l:
            self._q.put(i, False)

    def get(self):
        return self._q.get()


def match(x, y):
    free_x = set(x)
    res = {}
    while free_x:
        m = free_x.pop()
        w = x[m].get()
        if w not in res:
            res[w] = m
        else:
            print(res)
            if y[w].index(res[w]) > y[y].index(m):
                d = res.pop(y, None)
                free_x.add(d)
                res[w] = m
            else:
                free_x.add(m)

    print("\n".join(map(str, [(i, res[i]) for i in res])))

if __name__ == "__main__":
    a = {"A": q("YXZ"), "B": q("ZYX"), "C": q("XZY")}
    b = {"X": list("BAC"), "Y": list("CBA"), "Z": list("ACB")}
    match(a, b)
