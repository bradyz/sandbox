n = int(input())
slimes = list()
for _ in range(n):
    slimes.append(1)
    while len(slimes) > 1 and slimes[-1] == slimes[-2]:
        slimes.pop()
        slimes[-1] += 1
print(" ".join(map(str, slimes)))
