def suspect(b, t, u, n):
    prod = 1
    while u:
        if u & 1:
            prod = (prod*b) % n
        b = (b * b) % n
        u //= 2
    if prod == 1:
        return True
    for i in range(1, t + 1):
        if prod == n-1:
            return True
        prod = (prod * prod) % n
    return False


def isprime(n):
    k = n - 1
    t = 0

    while not (k % 2 == 0):
        t += 1
        k //= 2
    for m in [2, 3, 5, 7]:
        if n > m and n % m == 0:
            return False
    if suspect(61, t, k, n) and suspect(7, t, k, n) and suspect(2, t, k, n):
        return True
    return False


for x in range(1, 1000):
    if isprime(x):
        print(x)
