from sys import maxsize as MAXINT

n = int(input())
c = list(map(int, input().split()))
d = list(map(int, input().split()))
v = [[c[i], d[i]] for i in range(n)]

v.sort(key=lambda x: (x[0], -x[1]))

c = list(x[0] for x in v)
d = list(x[1] for x in v)

print(v)

for i in range(1, n):
    v[i][1] += v[i-1][1]

print(v)

r = MAXINT

i = 1

while i < n+1:
    j = 0
    while i-1+j < n and v[i-1][0] == v[i-1+j][0]:
        print(i, j, r)
        if j == 0:
            print("a")
            if i-1 == 0:
                r = v[n-1][1] - v[i-1][1]
            else:
                r = min(r, v[n-1][1] - (d[i-1]))
        elif j == 1:
            print("b")
            if i-2 == 0:
                r = min(r, v[n-1][1] - v[i-1+j][1])
            else:
                r = min(r, v[n-1][1] - (d[i-1]+d[i]+d[i-2]))
        else:
            print("c")
            if i-2 == 0:
                r = min(r, v[n-1][1] - v[i-1+j][1])
            else:
                r = min(r, v[n-1][1] - (v[i-1+j][1]-v[i-2-2*j][1]))
        j += 1
    i += max(1, j)

print(r)
