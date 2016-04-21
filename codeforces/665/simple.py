s = list(input())
n = len(s)
if n >= 2:
    while s[1] == s[0]:
        if ord(s[0]) + 1 <= ord("z"):
            s[0] = chr(ord(s[0]) + 1)
        else:
            s[0] = chr(ord(s[0]) - 1)
for i in range(n):
    if s[i] == s[i-1]:
        c = ord("a")
        flag = True
        while flag:
            flag = False
            for j in range(max(i-2, 0), min(i+2, n)):
                if j == i:
                    continue
                if ord(s[j]) == c:
                    flag = True
            if flag:
                c += 1
        s[i] = chr(c)
print("".join(s))
