# 400A: Inna and Choose Options
# Start Time: 11:54 p.m. 4-30-15
# End Time: 12:49 a.m. 5-1-15


def solve(c, n=12):
    r = set()
    for i in [1, 2, 3, 4, 6, 12]:
        win = False
        j = 12 // i
        for n in range(j):
            col = True
            for k in range(n, 12, j):
                col = col and c[k]
            win = win or col
        if win:
            r.add(i)

    return str(len(r)) + " " + " ".join([str(i)+"x"+str(12//i) for i in r])

if __name__ == "__main__":
    for _ in range(int(input())):
        board = [v == "X" for v in input()]
        print(solve(board, 12))
