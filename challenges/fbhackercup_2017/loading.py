def solve(c):
    c.sort()
    result = 0
    i = 0
    j = len(c)-1
    while i <= j:
        x = c[j]
        while x < 50 and i < j:
            x += c[j]
            i += 1
        j -= 1
        if x >= 50:
            result += 1
    return result


for i in range(1, int(input())+1):
    c = [int(input()) for _ in range(int(input()))]
    print("Case #%d: %s" % (i, solve(c)))
