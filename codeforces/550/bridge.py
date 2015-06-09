k = int(input())

if k % 2 == 0:
    print("NO")
else:
    print("YES")
    if k == 1:
        print(2, 1)
        print(1, 2)
    else:
        n = 2 + (k - 1) * 4
        print(n, n * k // 2)
        print(1, 2 * k)
        for i in range(2, k + 1):
            for j in range(k + 1, 2 * k):
                print(i, j)
                print(i + 2 * k - 1, j + 2 * k - 1)
            print(1, i)
            print(2 * k, i + 2 * k - 1)
        for i in range(k + 1, 2 * k, 2):
            print(i, i + 1)
            print(i + 2 * k - 1, i + 2 * k)
