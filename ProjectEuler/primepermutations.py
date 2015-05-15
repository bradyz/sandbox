from consecutiveprimesum import primes_below
from collections import Counter


def is_perm(a, b):
    x = {}
    y = {}
    for v, w in zip(str(a), str(b)):
        if v in x:
            x[v] += 1
        else:
            x[v] = 1
        if w in y:
            y[w] += 1
        else:
            y[w] = 1
    return x == y


# cheeky
def is_perm1(a, b):
    return Counter(a) == Counter(b)


def solve(n):
    p = primes_below(n, low=1000)
    s = set(p)
    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            t = p[j]+p[j]-p[i]
            if is_perm(p[i], p[j]) and t in s and is_perm(p[i], t):
                print("".join(map(str, [p[i], p[j], t])))

if __name__ == "__main__":
    solve(10000)
