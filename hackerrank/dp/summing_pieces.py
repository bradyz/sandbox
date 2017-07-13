MOD = int(1e9) + 7

input()
c = list(map(int, input().split()))
n = len(c)

result = 0

for k in range(1, n + 1):
    mult = pow(2, n, MOD) - pow(2, n-k, MOD)
    mult += pow(2, k-1, MOD) * (pow(2, n-k, MOD) - 1)

    result += int(mult) * c[k-1]
    result %= int(1e9) + 7

print(result)
