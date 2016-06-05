def lex_permutation(suf, pre=[], used=set()):
    if len(suf) == len(pre):
        yield pre
    for val in sorted(set(suf) - used):
        used.add(val)
        for rest in lex_permutation(suf, pre + [val], used):
            yield rest
        used.remove(val)

c = 1
for b in lex_permutation(range(10)):
    if c == int(1e6):
        print("".join(map(str, b)))
        break
    c += 1
