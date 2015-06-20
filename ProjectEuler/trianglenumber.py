def num_div(n):
    r = 0
    for i in range(1, n+1):
        if n % i == 0:
            r += 1
    return r
c = 0
z = 1
while num_div(c) < 500:
    c += z
    z += 1
print(c)
print(num_div(c))
