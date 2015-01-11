import sys


def marked_map(d_map, side):
    tmp_map = d_map

    for x in range(1, side - 1):
        for y in range(1, side - 1):
            cur = d_map[x][y]
            if cur > d_map[x - 1][y] and cur > d_map[x + 1][y]:
                if cur > d_map[x][y - 1] and cur > d_map[x][y + 1]:
                    tmp_map[x][y] = "X"

    for row in range(side):
        print(''.join([str(x) for x in tmp_map[row]]))
    return

if __name__ == "__main__":
    dep_map = []
    for i, line in enumerate(sys.stdin):
        if i == 0:
            side_len = int(line.strip("\n"))
        elif i > 0:
            tmp_line = [int(x) for x in line.strip("\n")]
            dep_map.append(tmp_line)

    marked_map(dep_map, side_len)
