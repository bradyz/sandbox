c = str(input())
n = len(c)
x = [i for i in range(n-1) if c[i:i+2] == "AB"]
y = [i for i in range(n-1) if c[i:i+2] == "BA"]
if x and y and (x[0] < y[-1] - 1 or y[0] < x[-1] - 1):
    print("YES")
else:
    print("NO")
