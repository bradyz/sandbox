def is_anagramA(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False


def is_anagramB(a, b):
    aDict = {}
    bDict = {}
    for x in str(a):
        if x in aDict:
            aDict[x] += 1
        else:
            aDict[x] = 1
    for x in str(b):
        if x in bDict:
            bDict[x] += 1
        else:
            bDict[x] = 1
    if aDict == bDict:
        return True
    else:
        return False

if __name__ == "__main__":
    lines = []
    with open('anagram-input.txt', 'r') as f:
        lines = f.readlines()

    for x, n in enumerate(lines):
        if x % 2 == 0:
            strA = n.split()
        else:
            strB = n.split()
            print is_anagramB(strA, strB)
