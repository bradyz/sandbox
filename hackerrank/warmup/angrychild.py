import sys


def most_fair(my_list, num):
    sorted_list = sorted(my_list)
    min_diff = sorted_list[-1] - sorted_list[0]

    for i, x in enumerate(range(num - 1, len(sorted_list))):
        tmp = sorted_list[x] - sorted_list[i]
        if tmp < min_diff:
            min_diff = tmp

    return min_diff

if __name__ == "__main__":
    candies = []
    k = 0
    for i, line in enumerate(sys.stdin):
        if i == 1:
            k = int(line.strip("\n"))
        if i > 1:
            candies.append(int(line.strip("\n")))

    print(str(most_fair(candies, k)))
