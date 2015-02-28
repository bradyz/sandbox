import sys


def max_toys(n, k):
    n = sorted(n)
    tmp = 0
    for val in n:
        if k - val >= 0:
            tmp += 1
            k -= val
    return tmp

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            arg = line.split()
            money = int(arg[1])
        else:
            prices = [int(x) for x in line.split()]
            print(max_toys(prices, money))
