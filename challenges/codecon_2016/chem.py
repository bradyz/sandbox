n = int(input())
dependencies = dict()
go_to = dict()
count = dict()
for _ in range(n):
    line = input().split()
    x = line[0]
    if x not in dependencies:
        dependencies[x] = set()
    for y in line[2:]:
        if y not in go_to:
            go_to[y] = set()
        go_to[y].add(x)
        dependencies[x].add(y)
        count[x] = count.get(x, 0) + 1
can = True
for current in input().split():
    if len(dependencies.get(current, set())) != 0:
        can = False
        break
    for to in go_to.get(current, set()):
        if current in dependencies.get(to, set()):
            dependencies[to].remove(current)
# print(dependencies)
# print(count)
# print(can)
if can:
    print("SAFE!")
else:
    print("BOOM!")
