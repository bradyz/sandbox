not_in = set(["pin", "pins", "pinned", "pinning", "pinner", "pinners"])

for _ in range(int(input())):
    c = input().lower().split()
    r = 0
    for v in c:
        if v not in not_in and "pin" in v:
            r += 1
    print(r)
