from consecutiveprimesum import primes_below as pb


def solve(n):
    p = pb(n, low=1)
    o = [i for i in sorted(list(set(range(n)) - set(p))) if i % 2 == 1]
    s = set([i**2 for i in range(1, n)])
    found = True
    i = 0

    while found:
        found = False
        j = 0
        while j < len(p) and p[j] < o[i]:
            if (o[i] - p[j]) / 2 in s:
                found = True
                break
            j += 1
        if not found:
            print(o[i])
        i += 1

    return 0

if __name__ == "__main__":
    solve(10000)
