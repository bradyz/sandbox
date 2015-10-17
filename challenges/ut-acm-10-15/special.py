def pf(n):
    for i in range(1, n+1):
        if n % i == 0:
            s[n].append(i)

s = [list() for _ in range(1001)]

p = [True for _ in range(1001)]
p[0] = False
p[1] = False

for i in range(1001):
    if p[i]:
        for j in range(i+i, 1001, i):
            p[j] = False

for i in range(1001):
    pf(i)

for _ in range(int(input())):
    r = 0
    for i in range(1, int(input())+1):
        if len(s[i]) == 4 and p[s[i][1]] and p[s[i][2]]:
            r += 1
    print(r)

r = 0
for i in range(1001):
    if len(s[i]) == 4 and p[s[i][1]] and p[s[i][2]]:
        r += 1
        print(i, s[i])
print(r)
