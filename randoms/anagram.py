import collections


def is_anagramA(a, b):
    if sorted(str(a)) == sorted(str(b)):
        return True
    else:
        return False


def is_anagramB(a, b):
    aDict = collections.Counter()
    bDict = collections.Counter()
    for x in str(a):
        aDict[x] += 1
    for x in str(b):
        bDict[x] += 1
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
            print "Sort: " + str(is_anagramA(strA, strB))
            print "Dict: " + str(is_anagramB(strA, strB))
