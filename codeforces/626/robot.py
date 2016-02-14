n = int(input())
s = input()

ret = 0
for i in range(n):
    for j in range(i+1, n+1):
        count = {}
        for k in range(i, j):
            count[s[k]] = count.get(s[k], 0) + 1
        eq = len(count) > 1
        if "U" in count or "D" in count:
            if "D" not in count or "U" not in count:
                eq = False
            else:
                eq &= count["U"] == count["D"]
        if "L" in count or "R" in count:
            if "R" not in count or "L" not in count:
                eq = False
            else:
                eq &= count["L"] == count["R"]
        ret += eq
print(ret)
