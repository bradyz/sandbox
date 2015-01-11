import sys


def num_div(to_div):
    div_list = str(to_div)
    count = 0
    for x in div_list:
        x_num = int(x)
        if x_num != 0 and to_div % x_num == 0:
            count += 1
    return count


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            parsed = int(line.strip("\n"))
            print(num_div(parsed))
