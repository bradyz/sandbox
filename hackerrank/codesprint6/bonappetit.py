n, k = map(int, input().split())
c = list(map(int, input().split()))
x = int(input())
d = (sum(c) - c[k]) // 2
if d == x:
    print("Bon Appetit")
else:
    print(x - d)
