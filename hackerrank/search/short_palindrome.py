MOD = int(1e9) + 7


def solve(c):
    ans = [0 for _ in range(26)]
    freq = [0 for _ in range(26)]
    ji = [[0 for _ in range(26)] for _ in range(26)]

    result = 0

    for i in c:
        result += ans[i]
        result %= MOD

        for j in range(26):
            ans[j] += ji[j][i]
            ans[j] %= MOD

        for j in range(26):
            ji[j][i] += freq[j]
            ji[j][i] %= MOD

        freq[i] += 1
        freq[i] %= MOD

    return result


if __name__ == '__main__':
    print(solve([ord(x) - ord('a') for x in input()]))
