x1, v1, x2, v2 = map(int, input().split())
for i in range(1, 10001):
    if (v2 * i + (x2 - x1)) % v1 == 0 and (v2 * i + (x2 - x1)) // v1 == i:
        print("YES")
        break
else:
    print("NO")
