import sys


def all_comb(num, a_val, b_val):
    result = []

    for x in range(num):
        y = num - x - 1
        tmp = a_val * x + b_val * y
        result.append(tmp)

    result.sort()
    str_res = ""

    for x in result:
        str_res += str(x) + " "

    return str_res


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            if i % 3 == 1:
                n = int(line.strip("\n"))
            elif i % 3 == 2:
                a = int(line.strip("\n"))
            elif i % 3 == 0:
                b = int(line.strip("\n"))
                print(all_comb(n, a, b))
