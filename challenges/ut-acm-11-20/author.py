def poss(k):
    for i in range(2**k):
        b = bin(i).lstrip("0b")
        c = k - len(b)
        yield [x == "1" for x in "0" * c + bin(i).lstrip("0b")]

for _ in range(int(input())):
    n = int(input())
    r = 0
    words = [input() for _ in range(n)]
    for v in poss(n):
        tmp = ""
        for i in range(len(v)):
            if v[i]:
                tmp += words[i]
        if tmp == "".join(reversed(tmp)):
            r += 1
    print(r-1)
