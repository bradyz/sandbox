def factors(t):
    i = 1
    r = 0
    while i * i <= t:
        if t % i == 0:
            if t // i == i:
                r += 1
            else:
                r += 2
        i += 1
    print(r)
    return r

c = 0
for x in range(1, int(1e9)):
    c += x
    if factors(c) > 500:
        print(c)
        break
