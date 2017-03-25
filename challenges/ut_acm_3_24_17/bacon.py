from bisect import bisect


if __name__ == "__main__":
    n = int(input())
    m = list(map(int, input().split()))
    p = list(map(int, input().split()))
    p.sort()

    have = 0

    for i in range(n):
        have += m[i]

        j = bisect(p, have)

        if j > 0:
            have -= p[j-1]

    print(have)
