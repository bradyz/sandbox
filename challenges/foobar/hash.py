def answer(d):
    c = [0 for v in d]
    for i in range(len(d)):
        t = 0
        if i == 0:
            t = d[i] // 129
        else:
            for j in range(1, 256):
                t = (d[i] ^ c[i-1]) * j
                if d[i] == ((t * 129) ^ c[i-1]) % 256:
                    break
        c[i] = t % 256
    return c

answer(map(int, raw_input().split()))
answer(map(int, raw_input().split()))
