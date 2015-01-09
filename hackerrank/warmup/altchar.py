import sys


def num_del(my_str):
    count = 0
    i = 1
    new_str = my_str
    prev = my_str[0]

    while i < len(new_str):
        if new_str[i] == prev:
            count += 1
            tmp_str = new_str[:i] + new_str[i+1:]
            new_str = tmp_str
        else:
            prev = new_str[i]
            i += 1

    return count


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            in_str = line.strip('\n')
            print(str(num_del(in_str)))
