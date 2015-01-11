import sys
import fractions
import itertools


def has_common(my_list):
    has_gcd = True
    my_list = set(my_list)
    for n in itertools.combinations(my_list, 2):
        tmp = fractions.gcd(n[0], n[1])
        if tmp == 1:
            has_gcd = False

    if not has_gcd:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            if i % 2 == 0:
                parsed = [int(x) for x in line.split()]
                print(has_common(parsed))
