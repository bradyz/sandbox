def answer(d, c):
    d = d.split()
    r = (0, len(d))
    for i in range(len(d)):
        for j in range(i, len(d)):
            if not set(c) - set(d[i:j+1]):
                if j+1-i < r[1] - r[0]:
                    r = (i, j+1)
    return " ".join(d[r[0]:r[1]])

print(answer(raw_input(), raw_input().split()))
