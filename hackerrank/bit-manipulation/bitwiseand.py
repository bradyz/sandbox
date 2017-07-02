def solve(n, k):
    if k-1 | k <= n:
        return k-1
    return k-2


for _ in range(int(input())):
    n, k = map(int, input().split())

    print(solve(n, k))
