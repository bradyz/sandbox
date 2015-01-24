import sys


def has_stolen(num, val, low, up):
    print(num, val, low * num, up * num)
    if val >= (num * low) and val <= (num * up):
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            args = [int(x) for x in line.split()]
            num_bags = args[0]
            money = args[1]
            lower = args[2]
            upper = args[3]
            print(has_stolen(num_bags, money, lower, upper))
