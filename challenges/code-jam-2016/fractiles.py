from itertools import product


def step(cur, init):
    ret = list()
    for char in cur:
        if char == "G":
            ret.append("G" * len(init))
        else:
            ret.append(init)
    return "".join(ret)


def generate(k, c, s):
    for seed in ["".join(x) for x in product("GL", repeat=k)]:
        for level in range(1, c+1):
            if level == 1:
                tmp = seed
            else:
                tmp = step(tmp, seed)
            if level == c:
                yield tmp


def check(ret, generated):
    found = [False for _ in generated]
    for v in ret:
        for i, f in enumerate(generated):
            if f[v-1] == "G":
                found[i] = True
    if found.count(False) > 1 or len(ret) > s:
        print("test:", k, c, s)
        print(len(ret), s, found)


for t in range(1, int(input()) + 1):
    k, c, s = map(int, input().split())
