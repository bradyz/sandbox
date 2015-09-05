def solve(w):
    def sieve():
        c = [True for _ in range(0, n+1)]
        c[0] = False
        c[1] = False
        for i in range(2, n+1):
            for j in range(i+i, n+1, i):
                c[j] = False
        return c

    n = int(w)
    c = sieve()
    n = len(w)

    for i in range(n):
        for j in range(i, n):
            if c[int(w[i:j+1])]:
                return "YES"
    return "NO"

for _ in range(int(input())):
    print(solve(input()))
