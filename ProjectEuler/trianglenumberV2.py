def num_div(n):
    r = 1
    x = 2
    while n > 1:
        t = 0
        while n % x == 0:
            t += 1
            n = n // x
        if t > 0:
            r *= (t + 1)
        x += 1
    return r


def triangle_numbers():
    c = 1
    z = 2
    while True:
        yield c
        c += z
        z += 1

for x in triangle_numbers():
    if num_div(x) > 500:
        print(x)
        break
