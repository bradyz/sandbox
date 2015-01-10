import sys


def avg_val(g_list, b):
    num_jars = b
    total_beans = 0

    for line in g_list:
        num_fill = line[1] - line[0] + 1
        num_beans = line[2]
        total_beans += (num_beans * num_fill)

    return total_beans / num_jars

if __name__ == "__main__":
    given_list = []
    for i, line in enumerate(sys.stdin):
        if i == 0:
            tmp = [int(x) for x in line.strip("\n").split()]
            beans = tmp[0]

        elif i > 0:
            given = [int(x) for x in line.strip("\n").split()]
            given_list.append(given)
    print(avg_val(given_list, beans))
