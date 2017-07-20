def alpha(c):
    return ord(c) - ord('a') + 1


def solve(s):
    scores = set()

    scores.add(alpha(s[0]))

    x = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            x += 1
        else:
            x = 1

        scores.add(x * alpha(s[i]))

    return scores


if __name__ == '__main__':
    scores = solve(input())

    for _ in range(int(input())):
        if int(input()) in scores:
            print('Yes')
        else:
            print('No')
