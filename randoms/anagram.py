def is_anagramA(a, b):
    return sorted(str(a)) == sorted(str(b))


def is_anagramB(a, b):
    from collections import Counter
    return Counter(a) == Counter(b)


def is_anagramC(a, b):
    xor = 0
    for u, v in zip(a, b):
        xor ^= ord(u) ^ ord(v)
    return xor == 0

if __name__ == "__main__":
    lines = []

    with open('anagram-input.txt', 'r') as f:
        lines = f.readlines()

    funcs = [is_anagramA, is_anagramB, is_anagramC]

    for x, n in enumerate(lines):
        if x % 2 == 0:
            strA = n.strip("\n")
        else:
            strB = n.strip("\n")
            print("\n".join(map(lambda x: str(x(strA, strB)), funcs)))
