n, m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
letter = {"a": set(), "b": set(), "c": set()}
for u in range(1, n+1):
    # if u is b
    if len(graph[u]) == n-1:
        letter["b"].add(u)
inconsistent = False
# looks for first element and calls it and all its neighbors "a"
for u in range(1, n+1):
    if u in letter["b"]:
        continue
    letter["a"].add(u)
    for v in range(1, n+1):
        if u == v:
            continue
        elif v in letter["b"]:
            continue
        elif v in graph[u]:
            letter["a"].add(v)
        else:
            letter["c"].add(v)
    break
# remaining elements should all be "c"
for u in range(1, n+1):
    if u in letter["b"]:
        continue
    for v in range(u+1, n+1):
        if v in letter["b"]:
            continue
        elif v in graph[u]:
            # neighbor should be the same
            if (u in letter["a"]) ^ (v in letter["a"]):
                inconsistent = True
        else:
            # neighbor should not be the same
            if not ((u in letter["a"]) ^ (v in letter["a"])):
                inconsistent = True
if not inconsistent:
    print("Yes")
    res = ["" for _ in range(n)]
    for char, indices in letter.items():
        for i in indices:
            res[i-1] = char
    print("".join(map(str, res)))
else:
    print("No")
