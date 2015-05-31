n = int(input())
c = sorted(map(int, input().split()))
i = 0
j = n-1
r = 0
while i <= j:
    val = c[j]
    while i <= j and val + c[i] <= 4:
        val += c[i]
        i += 1
    else:
        j -= 1
    r += 1
print(r)
