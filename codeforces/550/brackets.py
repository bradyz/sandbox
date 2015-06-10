n = int(input())
c = list(map(int, input().split()))
idx = [i for i in range(n) if c[i] == 0]
one = [i for i in range(n) if c[i] == 1]

if len(idx) >= 1 and idx[-1] == n-1:
    if len(idx) >= 2 and idx[-2] == n-2:
        if len(idx) >= 3 and idx[-3] <= n-3:
            if idx[0] == 0:
                print("YES")
                r = ""
                for i in range(n):
                    if i == 1:
                        r += "("
                    r += str(c[i])
                    if i == n-2:
                        r += ")"
                    if i != n-1:
                        r += "->"
                print(r)
            else:
                print("YES")
                r = ""
                if idx[-2]-1 == 0:
                    for i in range(n):
                        if i == 0:
                            r += "("
                        r += str(c[i])
                        if i == idx[-2]-1:
                            r += ")"
                        if i != n-1:
                            r += "->"
                else:
                    for i in range(n):
                        if i == 0:
                            r += "("
                        elif i == idx[0]:
                            r += "("
                        elif i == idx[0] + 1:
                            r += "("
                        r += str(c[i])
                        if i == idx[-1] - 1:
                            r += "))"
                        elif i == idx[0]-1:
                            r += ")"
                        if i != n-1:
                            r += "->"
                print(r)
        else:
            print("NO")
    else:
        print("YES")
        print("->".join(map(str, c)))
else:
    print("NO")
