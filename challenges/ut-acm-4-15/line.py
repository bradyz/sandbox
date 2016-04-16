from itertools import permutations, product


for _ in range(int(input())):
    p, b = map(int, input().split())
    c = list(map(int, input().split()))
    s = [chr(ord("A") + int(i)) for i in range(p)]
    d = list()
    for _ in range(b):
        not_allowed = "".join(input())
        num_stars = not_allowed.count("*")
        if num_stars > 0:
            tmp = list(not_allowed)
            idx = [i for i in range(len(not_allowed)) if not_allowed[i] == "*"]
            for gen in product(s, repeat=num_stars):
                for i, char in zip(idx, gen):
                    tmp[i] = char
                d.append("".join(tmp))
        else:
            d.append(not_allowed)
    for i in range(p):
        s[i] *= c[i]
    ret = set()
    for x in permutations("".join(s)):
        z = "".join(x)
        can = True
        for y in d:
            if y in z:
                can = False
        if can:
            ret.add(z)
    if len(ret) == 0:
        print("FIGHT")
    else:
        for x in sorted(ret):
            print(x)
    print()
