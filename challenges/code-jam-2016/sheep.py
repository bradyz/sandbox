for t in range(int(input())):
    n = int(input())
    if n == 0:
        print("Case #%d: INSOMNIA" % (t+1))
        continue
    seen = set()
    k = 1
    while len(seen) != 10:
        seen |= {x for x in str(n * k)}
        k += 1
    print("Case #%d: %d" % (t+1, n * (k - 1)))
