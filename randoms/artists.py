import sys
from collections import defaultdict


def matches(artists):
    fp = {}
    res = set()
    for art in artists:
        if len(artists[art]) > 50:
            fp[art] = artists[art]

    for i in fp:
        for j in fp:
            if i != j:
                if len(fp[i] & fp[j]) >= 50 and str(sorted([i, j])) not in res:
                    res.add(str(sorted([i, j])))
    print(res)

if __name__ == "__main__":
    occ = defaultdict(set)
    for i, line in enumerate(sys.stdin):
        tmp = line.split(",")
        for art in tmp:
            occ[art].add(i)
    matches(occ)
