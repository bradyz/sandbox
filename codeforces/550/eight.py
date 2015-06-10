c = list(input())
n = len(c)
f = False

for i in range(n):
    if int(c[i]) % 8 == 0:
        f = True
        print("YES")
        print(c[i])
        break

if not f:
    for i in range(n):
        for j in range(i+1, n):
            t = int(c[i]+c[j])
            if not f and t % 8 == 0:
                f = True
                print("YES")
                print(t)
                break

if not f:
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                t = int(c[i]+c[j]+c[k])
                if not f and t % 8 == 0:
                    f = True
                    print("YES")
                    print(t)
                    break

if not f:
    print("NO")
