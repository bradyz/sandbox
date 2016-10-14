def lex(a, b):
    s = [a, b]
    t = list(sorted(s))
    return (s == t)


def less(a, b):
    x1, y1 = a.split(" ")
    x2, y2 = b.split(" ")
    if y1 == y2:
        return lex(x1, x2)
    elif lex(y1, y2):
        return True
    return False


for _ in range(int(input())):
    n = int(input())
    names = [str(input()) for _ in range(n)]
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if less(names[j], names[i]):
                dp[i] = max(dp[i], dp[j] + 1)
    print(n - max(dp))
