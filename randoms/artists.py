import sys
from collections import defaultdict


def matches(artists):
    fp = {}
    res = set()

    for art in artists:
        if len(artists[art]) > 50:
            fp[art] = artists[art]

    for i in sorted(fp):
        for j in sorted(fp):
            if i < j and len(fp[i] & fp[j]) >= 50:
                    res.add(str((i, j)))

    for a in sorted(res):
        print(a)

if __name__ == "__main__":
    occ = defaultdict(set)
    for i, line in enumerate(sys.stdin):
        for art in line.split(","):
            occ[art].add(i)
    matches(occ)
