def valid(word):
    if len(word) != len(str(int(word))):
        return False
    elif int(word) > 100:
        return False
    return True


def solve(num_students, word):
    word_len = len(word)
    dp = [[-1 for _ in range(word_len+1)] for _ in range(num_students+1)]
    dp[0][0] = 0
    for i in range(1, word_len+1):
        for j in range(1, num_students+1):
            for k in range(1, 4):
                if j-1 < 0 or i-k < 0:
                    continue
                elif dp[j-1][i-k] == -1:
                    continue
                elif not valid(word[i-k:i]):
                    continue
                dp[j][i] = max(dp[j][i], int(word[i-k:i]) + dp[j-1][i-k])
    print(int(dp[num_students][word_len] / num_students + 0.5))


for _ in range(int(input())):
    x, y = map(int, input().split())
    solve(x, str(y))
