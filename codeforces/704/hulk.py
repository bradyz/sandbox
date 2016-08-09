n = int(input())
r = list()
for i in range(n):
    if i % 2 == 0:
        r.append("I hate")
    else:
        r.append("I love")
    if i == n-1:
        r.append("it")
    else:
        r.append("that")
print(" ".join(r))
