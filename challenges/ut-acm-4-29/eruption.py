for _ in range(int(input())):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    print(max(c) + k)
