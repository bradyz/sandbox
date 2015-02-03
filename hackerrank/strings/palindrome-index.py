import sys


def to_remove(string):
    string = list(string)
    indexes = {}
    odds = []

    if string == list(reversed(string)):
        return -1

    for idx, x in enumerate(string):
        if x not in indexes:
            indexes[x] = [idx]
        else:
            indexes[x].append(idx)

    for x in indexes:
        if len(indexes[x]) % 2 == 1:
            odds.append(indexes[x])

    for x in odds:
        for y in x:
            removed = string[:y] + string[y+1:]
            if removed == list(reversed(removed)):
                return y

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            parsed = line.strip("\n")
            index = to_remove(parsed)
            print(index)
