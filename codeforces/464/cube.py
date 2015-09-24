from math import sqrt


def solve():
    def check(n):
        s = set((b[0]+i*z, b[1]+j*z, b[2]+k*z) for i, j, k in
                ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1),
                 (1, 1, 0), (0, 1, 1), (1, 1, 1)))

        for v in c[:n]:
            if tuple(v) not in s:
                return False
            s.remove(tuple(v))

        return True

    def recur(n=0):
        if not check(n):
            return
        elif n == len(c):
            return c

        if recur(n+1):
            return c

        t = c[n]

        [1, 2, 3]

        for i in range(len(c[n])):
            for j in range(i, len(c[n])):
                c[n][j], c[n][i] = c[n][i], c[n][j]
                if recur(n+1):
                    return c
                c[n] = t

    b = list(sorted(c[0]))
    e = list(sorted(c[0]))

    for v in c[1:]:
        b = min(b, sorted(v))
        e = max(e, sorted(v))

    z = int(sqrt((e[0]-b[0])**2 + (e[1]-b[1])**2 + (e[2]-b[2])**2) / sqrt(3))

    print(b, e)

    s = set((b[0]+i*z, b[1]+j*z, b[2]+k*z) for i, j, k in
            ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1),
                (1, 1, 0), (0, 1, 1), (1, 1, 1)))

    print("\n".join(map(str, s)))

    if recur():
        print("YES")
        print("\n".join(map(lambda x: " ".join(map(str, x)), c)))
    else:
        print("NO")

if __name__ == "__main__":
    n = 8
    c = [list(int(x) for x in input().split()) for _ in range(n)]

    solve()
