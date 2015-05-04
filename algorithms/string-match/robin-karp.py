def RabinKarp(needle, haystack):
    l = len(needle)
    n = sum([int(val)*10**int(l-i-1) for i, val in enumerate(needle)])
    c = sum([int(val)*10**int(l-i-1) for i, val in enumerate(haystack[:l])])
    for i in range(l, len(haystack)):
        c = (c % 10**(l-1)) * 10 + int(haystack[i])
        print(c, n)
        if c == n:
            print(i)
    return i

if __name__ == "__main__":
    a = "343"
    b = "123234345"
    RabinKarp(a, b)
