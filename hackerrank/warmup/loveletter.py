import sys


def num_sub(my_str):
    num = 0

    if is_palin(my_str):
        return num

    for i in range(len(my_str) / 2):
        dif = 0
        dif = abs(ord(my_str[i]) - ord(my_str[len(my_str) - 1 - i]))
        num += dif

    return num


def is_palin(my_str):
    i = 0
    for i in range((len(my_str) / 2)):
        if my_str[i] != my_str[len(my_str) - 1 - i]:
            return False

    return True

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            print(str(num_sub(line.strip("\n"))))
