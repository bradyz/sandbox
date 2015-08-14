n, m = map(int, input().split())
if n == 1:
    print(n)
elif m > n // 2:
    print(m-1)
else:
    print(m+1)
