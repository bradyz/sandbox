import sys

def max_kills(g, x, y, n, m):
    max_num = 0

    for i in range(x - n):
        for j in range(y - m):
            tmp = 0
            for a in range(n):
                for b in range(m):
                    tmp += grid[i+a][j+b]
            max_num = max(max_num, tmp)

    return max_num


if __name__ == "__main__":
    num_tests = int(input())

    for test in range(num_tests):
        args = [int(x) for x in raw_input().split()]
        camps = args[0]
        wid = args[1]
        col = args[2]
        coors = []
        min_x = -sys.maxint + 1
        min_y = -sys.maxint + 1
        max_x = sys.maxint
        max_y = sys.maxint
        print(min_x, min_y)

        for camp in range(camps):
            tmp = [int(x) for x in raw_input().split()]
            x = tmp[0]
            y = tmp[1]
            num = tmp[0]
            coors.append((x, y, num))
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        x_size = max_x - min_x
        y_size = max_y - min_y

        grid = [[0 for i in range(x_size)] for j in range(y_size)]

        for coor in coors:
            grid[coor[0]][coor[1]] = coor[2]

        max_kills = max_kill(grid, x_size, y_size, wid, col)
        print(max_kills)
