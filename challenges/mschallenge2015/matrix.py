from functools import reduce
import sys

f = [list(line.strip("\n")) for line in sys.stdin]

pipes = []

for i in range(len(f)):
    for j in range(len(f[i])):
        if i == 0:
            if f[i][j] == "|":
                pipes.append(j)
        elif j in pipes:
            f[i][j] = "|"

f = list(map(lambda x: "".join(x), f))

m = []

for i in range(len(f)):
    for j in range(len(pipes) // 2):
        if i == 0:
            m.append([])
        if f[i][pipes[2*j]: pipes[2*j+1]].lstrip("|").replace(" ", ""):
            m[j].append(list(map(int, f[i][pipes[2*j]: pipes[2*j+1]].lstrip("|").split())))


def mmul(a, b):
    c = [[0 for j in range(len(b[0]))] for i in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

    return c

c = reduce(mmul, m)

m = -1
s = [0 for _ in range(len(c[0]))]

for i in range(len(c)):
    for j in range(len(c[i])):
        c[i][j] = str(c[i][j])
        s[j] = max(s[j], len(c[i][j]))

r = ""


for i in range(len(c)):
    r += " | "
    t = []
    for j in range(len(c[i])):
        t.append((s[j]-len(c[i][j])) * " " + str(c[i][j]))
    r += " ".join(t) + " | \n"

print(r.rstrip("\n"))
