n, m = map(int, input().split())
on = [False for _ in range(m+1)]
for _ in range(n):
    for x in list(map(int, input().split()))[1:]:
        on[x] = True
for i in range(1, m+1):
    if not on[i]:
        print("NO")
        break
else:
    print("YES")
