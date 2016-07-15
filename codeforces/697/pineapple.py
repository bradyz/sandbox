t, s, x = map(int, input().split())
if (t < x) and (x != t + 1 and x != t + 2) and ((x - t) % s == 0 or (x - t) % s == 1):
    print("YES")
else:
    print("NO")
