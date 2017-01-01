for _ in range(int(input())):
    a = input()
    b = input()
    n = len(a)
    m = len(b)

    dp = [[False for _ in range(n)] for _ in range(m)]

    for i in range(m):
        if a[i].isupper():
            if a[i] == b[0]:
                dp[0][i] = True
            break
        elif a[i].upper() == b[0]:
            dp[0][i] = True

    for i in range(1, m):
        idx = [j for j in range(n-1, -1, -1) if dp[i-1][j]]
        while idx:
            j = idx.pop() + 1
            while j < n:
                if a[j].isupper():
                    if a[j] == b[i]:
                        dp[i][j] = True
                    break
                elif a[j].upper() == b[i]:
                    dp[i][j] = True
                j += 1

    result = True

    for i in range(n-1, -1, -1):
        if dp[m-1][i]:
            break
        elif not dp[m-1][i]:
            if a[i].isupper():
                result = False
                break

    if result:
        print("YES")
    else:
        print("NO")
