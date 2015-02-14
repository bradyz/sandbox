import sys


def sortedby(new, unsorted):
    new_values = {}
    result = []
    unsorted = list(unsorted)
    for val, x in enumerate(new):
        new_values[val] = x
    for x in sorted(new_values.keys()):
        if new_values[x] in unsorted:
            oc = [ind for ind, a in enumerate(unsorted) if a == new_values[x]]
            for num in oc:
                result.append(unsorted[num])
    return "".join(result)


def sbimproved(new, unsorted):
    new = list(new)
    unsorted = list(unsorted)
    head = 0
    for c in new:
        for i in range(head, len(unsorted)):
            if unsorted[i] == c:
                unsorted[head], unsorted[i] = unsorted[i], unsorted[head]
                head += 1
    return unsorted

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i % 2 == 0:
            newalpha = line.strip("\n")
        else:
            tosort = line.strip("\n")
            res = sortedby(newalpha, tosort)
            another = sbimproved(newalpha, tosort)
            print(newalpha)
            print(tosort)
            print(res)
            print(another)
