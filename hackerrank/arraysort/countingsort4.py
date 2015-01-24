import sys
from collections import OrderedDict

if __name__ == "__main__":
    count = OrderedDict()
    exempt = []
    res = ""
    total = 0

    for i, line in enumerate(sys.stdin):
        if i == 0:
            total = int(line.strip("\n"))
        elif i > 0:
            args = line.split()

            if int(args[0]) not in count:
                count[int(args[0])] = [[args[1], i]]
            else:
                count[int(args[0])].append([args[1], i])

    for x in sorted(count.keys()):
        for y in count[x]:
            if y[1] <= total / 2:
                res += "- "
            else:
                res += str(y[0]) + " "

    print(res)
