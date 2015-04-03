args = [int(v) for v in input().split()]
shards = []

for _ in range(args[0]):
    shards.append(input().split())

for _ in range(args[1]):
    query = [v for v in input().split()]

    if query[2] != "-1":
        rel = list(filter(lambda x: x[1] == query[2], shards))
    else:
        rel = shards

    if query[1] == "id":
        print(sorted(rel, key=lambda x: x[0])[int(query[0])][0])
    elif query[1] == "size":
        print(sorted(rel, key=lambda x: int(x[2]))[int(query[0])][0])
    elif query[1] == "lm":
        print(sorted(rel, key=lambda x: int(x[3]))[int(query[0])][0])
    elif query[1] == "lr":
        print(sorted(rel, key=lambda x: int(x[4]))[int(query[0])][0])
