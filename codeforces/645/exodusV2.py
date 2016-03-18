n, k = map(int, input().split())
r = input()
s = [i for i in range(n) if r[i] == "0"]
ret = int(1e9)
win = int(1e9)
for i in range(k, len(s)):
    if s[i] - s[i-k] < win:
        win = s[i] - s[i-k]
        for x in range(i-k, i):
            ret = min(ret, max(s[x] - s[i-k], s[i] - s[x]))
print(ret)
