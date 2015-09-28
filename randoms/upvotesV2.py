def formula(n):
    return (n-1) * n // 2

if __name__ == "__main__":
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    a = [1 for v in c]

    for i in range(1, n):
        if c[i] >= c[i-1]:
            a[i] = min(a[i-1] + 1, k)

    a = list(map(formula, a))

    print(c)
    print(a)

    x = 0

    for i in range(1, k):
        x += a[i]
        if a[i] > a[i-1]:
            x -= a[i-1]

    print(x)

    for i in range(k, n):


