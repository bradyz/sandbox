n, bx = map(int, input().split())
xn = list(map(int, input().split()))
m, by = map(int, input().split())
yn = list(map(int, input().split()))
x = 0
for i in range(n):
    x += xn[n-1-i] * bx ** i
y = 0
for i in range(m):
    y += yn[m-1-i] * by ** i
if x == y:
    print("=")
elif x > y:
    print(">")
else:
    print("<")
