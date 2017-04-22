for _ in range(int(input())):
    n, m = map(int, input().split())
    found = set()
    for _ in range(m):
        u, v = map(int, input().split())
        found.add(v)
        found.add(u)

    if len(found) == n:
        print("YES")
    else:
        print("NO")
