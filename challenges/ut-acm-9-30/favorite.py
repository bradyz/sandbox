for _ in range(int(input())):
    orig = dict()
    freq = dict()
    words = list()
    for i, w in enumerate(input().split()):
        t = "".join(a.lower() for a in w if a.isalnum())
        orig[t] = i
        words.append(t)
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    print(", ".join(sorted(freq, key=lambda x: (-freq[x], -len(x), orig[x]))))
