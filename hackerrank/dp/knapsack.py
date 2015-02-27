import pprint
import sys


inf = (2 << 30) - 1


def opt(v, n, w):
    def _opt(_n, _w):
        if _w < 0:
            return -inf
        if _n == -1:
            return -inf

        if mem[_w][_n] != -1:
            return mem[_w][_n]

        res = max(_opt(_n, _w-1), _opt(_n-1, _w))
        res = max(res, _opt(_n, _w-v[_n])+v[_n])
        mem[_w][_n] = res

        print(v)
        pp.pprint(mem)

        return res

    mem = [[-1 for _ in range(n)] for _ in range(w+1)]

    for i in range(n):
        mem[0][i] = 0

    return _opt(n-1, w)


if __name__ == "__main__":
    sys.setrecursionlimit(15000)
    t = int(input())
    for _ in range(t):
        l1 = [int(v) for v in raw_input().split()]
        l2 = list(set([int(v) for v in raw_input().split()]))
        # l2 = [int(v) for v in raw_input().split()]
        num = len(l2)
        weight = l1[1]
        val = l2
        pp = pprint.PrettyPrinter()
        print(opt(val, num, weight))
