def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


n, a, b, p, q = map(int, input().split())
r = (n // a) * p + (n // b) * q
lcm = (a * b) // gcd(a, b)
print(lcm)
r -= (n // lcm) * min(p, q)
r += (n // lcm) * max(p, q)
print(r)
