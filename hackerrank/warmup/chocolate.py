import sys


def num_choco(p_list):
    money = p_list[0]
    cost = p_list[1]
    disc = p_list[2]
    num = 0

    while money >= cost:
        money -= cost
        num += 1

        if num % disc == 0:
            num += 1

    return num


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            parsed = [int(x) for x in line.split()]
            print(num_choco(parsed))
