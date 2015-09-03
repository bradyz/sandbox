n, m = map(int, input().split())
a, b = map(int, input().split())
c = list(sorted(map(int, input().split())))
d = list(sorted(map(int, input().split())))

if c[a-1] < d[-b]:
    print("YES")
else:
    print("NO")
