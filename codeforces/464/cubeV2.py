from itertools import permutations
from math import sqrt


def solve():
    def check(n):
        d = dict()

        for i in range(n):
            for j in range(i+1, n):
                x_1, y_1, z_1 = c[i]
                x_2, y_2, z_2 = c[j]
                t = sqrt((x_2-x_1)**2 + (y_2-y_1)**2 + (z_2-z_1)**2)
                d[t] = d.get(t, 0) + 1

        if len(set(map(tuple, c[:n]))) < n or len(d.values()) > 3:
            return False

        for i, v in enumerate(sorted(d.values())):
            if i == 0:
                if v > 4:
                    return False
            else:
                if v > 12:
                    return False

        return True

    def recur(n=0):
        if not check(n):
            return
        elif n == len(c):
            return c

        if recur(n+1):
            return c

        t = c[n]
        for v in permutations(c[n]):
            c[n] = v
            if recur(n+1):
                return c
        c[n] = t

    if recur():
        print("YES")
        print("\n".join(map(lambda x: " ".join(map(str, x)), c)))
    else:
        print("NO")

if __name__ == "__main__":
    n = 8
    c = [list(int(x) for x in input().split()) for _ in range(n)]

    solve()
