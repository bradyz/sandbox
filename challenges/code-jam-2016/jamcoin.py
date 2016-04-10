from itertools import product


def divisor(x):
    for p in primes:
        if x > p and x % p == 0:
            return p
    return None

if __name__ == "__main__":
    prime = [True for _ in range(10 ** 6 + 1)]
    prime[0] = False
    prime[1] = False
    primes = list()
    for i in range(2, len(prime)):
        if not prime[i]:
            continue
        primes.append(i)
        for j in range(i + i, len(prime), i):
            prime[j] = False
    for t in range(int(input())):
        n, j = map(int, input().split())
        ret = 0
        print("Case #%d:" % (t+1))
        for p in product("01", repeat=n-2):
            x = "1" + "".join(p) + "1"
            tmp = []
            for b in range(2, 11):
                d = divisor(int(x, b))
                if not d:
                    tmp = []
                    break
                tmp.append(d)
            if tmp:
                ret += 1
                print(x, " ".join(map(str, tmp)))
            if ret == j:
                break
