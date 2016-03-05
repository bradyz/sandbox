for _ in range(int(input())):
    word, k = input().split()
    k = int(k)
    res = []
    for char in word:
        new = (ord(char) - ord("A") + k) % 26
        res.append(chr(ord("A") + new))
    print("".join(map(str, res)))
