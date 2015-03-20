from collections import Counter


def is_anagramA(a, b):
    return sorted(str(a)) == sorted(str(b))


def is_anagramB(a, b):
    return Counter(a) == Counter(b)

if __name__ == "__main__":
    lines = []
    with open('anagram-input.txt', 'r') as f:
        lines = f.readlines()

    for x, n in enumerate(lines):
        if x % 2 == 0:
            strA = n.strip("\n")
        else:
            strB = n.strip("\n")
            print(strA, strB)
            print("Sort: " + str(is_anagramA(strA, strB)))
            print("Dict: " + str(is_anagramB(strA, strB)))
