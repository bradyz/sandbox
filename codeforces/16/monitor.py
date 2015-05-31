def gcd(i, j):
    if i == 0:
        return j
    else:
        return gcd(j % i, i)

a, b, c, d = map(int, input().split())

# reduce c, d to smallest integer terms
n = gcd(c, d)
c, d = c // n, d // n

# find a solution that fits within bounds
k = min(a // c, b // d)
print(c * k, d * k)
