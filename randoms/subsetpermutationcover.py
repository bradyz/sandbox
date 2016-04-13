from itertools import permutations, combinations


def cover(sub, to_cover):
    covered = [False for _ in to_cover]
    print(sub)
    for i, subset_perm in enumerate(to_cover):
        for s in sub:
            if covered[i]:
                break
            j = 0
            for x in s:
                if j < len(subset_perm) and subset_perm[j] == x:
                    j += 1
                if j == len(subset_perm):
                    covered[i] = True
                    break
        if not covered[i]:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    s = int(input())

    c = list(range(1, n+1))
    to_cover = {p for c in combinations(c, s) for p in permutations(c)}
    perms = [p for p in permutations(c)]

    for i in range(7, len(perms) + 1):
        for sub in combinations(perms, i):
            if cover(sub, to_cover):
                print(sub)
                break
