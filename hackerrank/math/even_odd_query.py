def solve():
    if x > y:
        return 'Odd'

    if x == y:
        if c[x-1] % 2 == 0:
            return 'Even'
        return 'Odd'

    if x < n and c[x] == 0:
        return 'Odd'
    elif c[x-1] % 2 == 0:
        return 'Even'

    return 'Odd'


n = int(input())
c = list(map(int, input().split()))

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(solve())
