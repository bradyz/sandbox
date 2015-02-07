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

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i % 2 == 0:
            newalpha = line.strip("\n")
        else:
            tosort = line.strip("\n")
            res = sortedby(newalpha, tosort)
            print(newalpha)
            print(tosort)
            print(res)
