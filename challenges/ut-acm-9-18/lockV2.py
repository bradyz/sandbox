def dfs(i):
    global r

    if i == len(q):
        r += 1
        return

    for j in range(v[i][0], v[i][1]+1):
        if i == 0:
            t[i] = j
            dfs(i+1)
        elif j >= t[i-1]:
            t[i] = j
            dfs(i+1)

for _ in range(int(input())):
    r = 0
    c = list(input())
    q = list(i for i, val in enumerate(c) if val == "?")
    left = type(c)(c)
    right = type(c)(c)

    if c[0] == "?":
        left[0] = '1'

    if c[-1] == "?":
        right[-1] = '9'

    for i in range(1, len(c)):
        if c[i] == "?":
            left[i] = left[i-1]
        else:
            left[i] = max(left[i-1], c[i])

        if c[len(c)-i-1] == "?":
            right[len(c)-i-1] = right[len(c)-i]
        else:
            right[len(c)-i-1] = max(right[len(c)-i], c[len(c)-i-1])

    v = list((int(left[i]), int(right[i])) for i in q)
    t = [0 for x in q]

    dfs(0)

    print(r)
