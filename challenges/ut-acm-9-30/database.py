for _ in range(int(input())):
    words = dict()
    for _ in range(int(input())):
        word = input()
        t = ord(word[0])
        for i in range(1, len(word)):
            t += abs(ord(word[i])-ord(word[i-1]))
        words[word] = t
    print(", ".join(map(lambda x: x[1],
                        sorted((v, k) for k, v in words.items()))))
