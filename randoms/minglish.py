def answer(words):
    alphabet = {char for word in words for char in word}
    g = {a: set() for a in alphabet}
    t = {a: 0 for a in alphabet}

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            x, y = words[i], words[j]
            for z in range(min(len(x), len(y))):
                if x[z] != y[z]:
                    if y[z] not in g[x[z]]:
                        t[y[z]] += 1
                        g[x[z]].add(y[z])
                    break

    s = [c for c in t if t[c] == 0]
    r = list()

    while s:
        c = s.pop()
        r.append(c)
        for v in g[c]:
            t[v] -= 1
            if t[v] == 0:
                s.append(v)

    return "".join(r)

words = ["ba", "ab", "cb"]
words = ["aa", "aab"]
print(answer(words))
