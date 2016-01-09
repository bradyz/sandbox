from bisect import bisect


for T in range(int(input())):
    N, P = map(int, input().split())
    prices = list(map(int, input().split()))

    prefix = [0] + prices[::]
    for i in range(1, N+1):
        prefix[i] += prefix[i-1]

    result = 0

    for i in range(1, N+1):
        prev = prefix[i-1]
        j = bisect(prefix, P + prev, i)
        result += j - i

    print("Case #" + str(T+1) + ": " + str(result))
