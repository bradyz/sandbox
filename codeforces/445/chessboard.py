# 445A: DZY Loves Chessboard
# Start Time: 6:59 p.m. 5-5-15
# End Time: 7:50 p.m. 5-5-15

if __name__ == "__main__":
    a = ["B", "W"]
    n, m = map(int, input().split())
    g = [input() for _ in range(n)]
    for i in range(n):
        print("".join([a[(i+j) % 2]
                       if g[i][j] == "." else "-" for j in range(m)]))
