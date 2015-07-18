def solve(c):
    c = map(lambda x: (sum(list(ord(v)-ord("a")+1 for v in x)), x), c)
    return [n[1] for n in sorted(c, key=lambda x: (-x[0], [-ord(y) for y in x[1]]))]

names = ["ab", "ba"]
print(solve(names))
