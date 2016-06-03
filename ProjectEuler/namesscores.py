names = input().split(",")
names.sort()
ret = 0
for i, val in enumerate(names):
    ret += (i + 1) * sum(ord(x) - ord("A") + 1 for x in val.strip("\""))
print(ret)
