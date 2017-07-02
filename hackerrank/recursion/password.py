import sys
sys.setrecursionlimit(10000)

def solve(c, d):
    dp = [True] + [False for _ in range(len(c))]

    #   c a t d o g
    # 1 0 0 0 0 0 0
    # 0 1 2 3 4

    for i in range(1, len(c)+1):
        for x in d:
            n = len(x)

            if n > i:
                continue

            if dp[i-n] and c[i-n:i] == x:
                dp[i] = True

    if not dp[-1]:
        return 'WRONG PASSWORD'

    result = list()
    cur = len(c)

    while cur != 0:
        for x in d:
            n = len(x)

            if n > cur:
                continue

            if dp[cur-n] and c[cur-n:cur] == x:
                result.append(x)
                cur = cur-n
                break

    return ' '.join(reversed(result))


for _ in range(int(input())):
    input()
    d = set(input().split())
    c = input()

    print(solve(c, d))
