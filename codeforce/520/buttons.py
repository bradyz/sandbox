n, m = map(int, input().split())
c = 0

while n < m:
    if m % 2 == 0:
        m //= 2
    else:
        m += 1
    c += 1

print(n - m + c)
