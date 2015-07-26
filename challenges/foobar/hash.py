def answer(d):
    c = [0 for v in d]
    for i in range(len(d)):
        t = 0
        if i == 0:
            for j in range(1, 256):
                t = d[i] * j
                if d[i] == (129 * t) % 256:
                    break
        else:
            for j in range(1, 256):
                t = (d[i] ^ c[i-1]) * j
                if d[i] == ((129 * t) ^ c[i-1]) % 256:
                    break
        c[i] = t % 256
    return c


def create(c):
    d = [0 for v in c]
    for i in range(len(c)):
        if i == 0:
            d[i] = ((129 * c[i]) ^ 0) % 256
        else:
            d[i] = ((129 * c[i]) ^ c[i-1]) % 256
    return d

for i in range(1):
    a = map(int, raw_input().split())
    print(a)
    print(create(a))
    print(answer(create(a)))
