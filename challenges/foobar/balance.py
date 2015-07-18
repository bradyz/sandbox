def solve(n):
    t = 0
    while 3**(t+1) < n:
        t += 1
    print(t)
    r = ["-" for _ in range(t+1)]
    while n != 0 and t >= 0:
        if abs(n) < 3 ** t:
            pass
        elif abs(n) > 3 ** t and abs(n) < 2 * 3 ** (t+1):
            r[t] = "L"
            if n > 0:
                n -= 3 ** (t+1)
            else:
                n += 3 ** (t+1)
        else:
            r[t] = "R"
            if n > 0:
                n -= 3 ** t
            else:
                n += 3 ** t
        t -= 1
        print(n, t, r)
    return r

print(solve(10))
