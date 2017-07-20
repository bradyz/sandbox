def solve(n, k, s):
    l = 0
    r = n-1

    spots = set()

    while l <= r:
        if s[l] != s[r]:
            spots.add((l, r))

        l += 1
        r -= 1

    if k < len(spots):
        return -1

    l = 0
    r = n-1

    while l <= r and k > 0:
        if l == r:
            if k >= 1:
                s[l] = 9

                k -= 1
        else:
            x = s[l] != 9
            y = s[r] != 9

            if (l, r) in spots:
                if k == len(spots):
                    m = max(s[l], s[r])

                    s[l] = m
                    s[r] = m

                    k -= 1
                elif k > len(spots):
                    if x:
                        s[l] = 9
                        k -= 1

                    if y:
                        s[r] = 9
                        k -= 1

                spots.remove((l, r))
            else:
                if k == len(spots):
                    pass
                elif x and y and k - 2 >= len(spots):
                    if x:
                        s[l] = 9
                        k -= 1

                    if y:
                        s[r] = 9
                        k -= 1
                elif x ^ y and k - 1 >= len(spots):
                    if x:
                        s[l] = 9
                        k -= 1

                    if y:
                        s[r] = 9
                        k -= 1

        l += 1
        r -= 1

    return ''.join(map(str, s))


n, k = map(int, input().split())
s = list(map(int, input()))

print(solve(n, k, s))
