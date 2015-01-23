import sys


def isUpper(c):
    if ord(c) < ord("a"):
        return True
    else:
        return False


def toLower(word):
    diff = ord("A") - ord("a")
    word = [i for i in word]
    for x in range(len(word)):
        if isUpper(word[x]):
            word[x] = chr(ord(word[x]) - diff)
    return "".join(map(str, word))

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i % 2 == 0:
            camel_word = line.strip("\n")
        else:
            correct = line.strip("\n")
            lower = toLower(camel_word)
            print("Correct: " + correct + " Answer: " + str(lower))
