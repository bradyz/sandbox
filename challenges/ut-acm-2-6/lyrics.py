for _ in range(int(input())):
    x, y, l = map(int, input().split())
    s = list()
    for _ in range(l):
        for word in input().split():
            r = ""
            for c in word.lower():
                if c.isalpha():
                    r += c
            if r:
                s.append(r)
    c = dict()
    for w in s:
        c[w] = c.get(w, 0) + 1
    r = 0
    for w in c:
        r += c[w] >= y
    if r >= x:
        print("WRITE")
    else:
        print("LET IT GO")
