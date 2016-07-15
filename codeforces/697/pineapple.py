t, s, x = map(int, input().split())
if x < t:
    print("NO")
elif x == t:
    print("YES")
elif x < t + 2:
    print("NO")
elif (x - t) % s == 0 or (x - t) % s == 1:
    print("YES")
else:
    print("NO")
