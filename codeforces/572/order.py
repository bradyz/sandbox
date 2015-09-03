n, m = map(int, input().split())
b = {}
s = {}

for _ in range(n):
    u, v, w = input().split()
    t = None

    if u == "B":
        t = b
    else:
        t = s

    t[int(v)] = t.get(int(v), 0) + int(w)

s_k = list(sorted(s.keys()))

for i in range(min(m, len(s_k))-1, -1, -1):
    print("S " + str(s_k[i]) + " " + str(s[s_k[i]]))

b_k = list(reversed(sorted(b.keys())))

for i in range(min(m, len(b_k))):
    print("B " + str(b_k[i]) + " " + str(b[b_k[i]]))
