x = input()
n = len(x)
r = 0
for i in range(n):
    t = int(x[i])
    r += t
    for j in range(i+1, n):
        t = t * 10 + int(x[j])
        r += t
print(r % int(1e9 + 7))
