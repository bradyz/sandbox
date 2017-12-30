s = input()
c = [0] + [0 for _ in s]

for i in range(len(s)):
    c[i+1] = c[i] + int(s[i] == 'B') * 2 - 1

l = c.index(min(c))
r = c.index(max(c))

if l > r:
    l, r = r, l

print(l+1, r)
