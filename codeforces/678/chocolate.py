def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


n, a, b, p, q = map(int, input().split())
lcm = (a * b) // gcd(a, b)
if p < q:
    r = (n // a) * p + (n // b) * q - (n // lcm) * p
else:
    r = (n // a) * p + (n // b) * q - (n // lcm) * q
print(r)
