for T in range(int(input())):
    N, P = map(int, input().split())
    prices = list(map(int, input().split()))

    prefix = [0] + prices[::]
    for i in range(1, N+1):
        prefix[i] += prefix[i-1]

    result = 0

    for i in range(N+1):
        for j in range(i+1, N+1):
            if prefix[j] - prefix[i] <= P:
                result += 1

    print("Case #" + str(T+1) + ": " + str(result))
