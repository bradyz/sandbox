def solve(c):
    l = 0
    r = 1
    s = set([c[0]])

    result = 1

    while r < len(c):
        while c[r] in s:
            s.remove(c[l])
            l += 1

        s.add(c[r])
        r += 1

        result = max(result, len(s))

    print(result)


for _ in range(int(input())):
    solve([int(input()) for _ in range(int(input()))])
