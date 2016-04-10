for t in range(int(input())):
    s = [(x == "+") for x in input()]
    n = len(s)
    j = n-1
    ret = 0
    while j >= 0:
        k = j
        while k >= 0 and s[k]:
            k -= 1
        for i in range(k, -1, -1):
            s[i] = not s[i]
        j = k
        if j >= 0:
            ret += 1
    print("Case #%d: %d" % (t+1, ret))
