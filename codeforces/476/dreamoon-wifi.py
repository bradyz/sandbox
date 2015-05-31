# 476B: Dreamoon and WiFi
# Start Time: 4:05 p.m. 4-30-15
# End Time: 5:00 p.m. 4-30-15

from functools import reduce
from collections import Counter


def nchoosek(n, k):
    if n-k+1 <= 1:
        return 1

    a = reduce(lambda x, y: x * y, range(1, n+1))
    b = reduce(lambda x, y: x * y, range(1, k+1))
    c = reduce(lambda x, y: x * y, range(1, n-k+1))

    return a / b / c

if __name__ == "__main__":
    x = input()
    y = input()

    x_c = Counter(x)
    y_c = Counter(y)

    if x_c == y_c:
        print("1.000000000000")
    else:
        diff = abs((x_c["+"] - x_c["-"]) - (y_c["+"] - y_c["-"]))
        q = 2 ** y_c["?"]

        if y_c["?"] < diff:
            print("0.000000000000")
        else:
            p = nchoosek(y_c["?"], max(x_c["+"]-y_c["+"], x_c["-"]-y_c["-"]))
            print("%.9f" % (p / q))
