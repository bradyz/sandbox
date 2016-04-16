for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(d):
        i, p = map(int, input().split())
        a[i-1] += p
    print(" ".join(map(str, a)))
