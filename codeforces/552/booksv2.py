n = int(input())
r = 0
for i in range(1, len(str(n))+1):
    if n >= 10 ** i:
        r += ((10 ** i - 1) - (10 ** (i-1) - 1)) * i
    else:
        r += (n - (10 ** (i - 1) - 1)) * i
print(r)
