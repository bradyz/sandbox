for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    m = int(input())
    d = list(map(int, input().split()))

    total_sum = sum(c) + sum(d)
    original = abs(sum(c) - sum(d))

    values = list(c + d)
    num = len(values)

    dp = [[False for _ in range(num+1)] for _ in range(total_sum+1)]

    for j in range(num+1):
        dp[0][j] = True

    for i in range(1, total_sum+1):
        for j in range(1, num+1):
            if values[j-1] < 0:
                continue
            elif not dp[i - values[j-1]][j-1] and not dp[i][j-1]:
                continue

            dp[i][j] = True

    best = 0

    for i in range(total_sum+1):
        if not dp[i][num]:
            continue

        if abs(i - (total_sum - i)) < abs(best - (total_sum - best)):
            best = i

    if original == abs(best - (total_sum - best)):
        print("BALANCED")
    else:
        print("UNBALANCED")
