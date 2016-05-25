n = int(input())
if n > 26:
    print(-1)
else:
    s = list(input())
    t = set(s)
    print(len(s) - len(t))
