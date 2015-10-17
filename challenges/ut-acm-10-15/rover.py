MAP = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (-1, 0)}
NEXT = {"N": "E", "S": "W", "E": "S", "W": "N"}

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m, r, q = map(int, input().split())
        rovers = [list(input().split()) for _ in range(r)]
        g = [input() for _ in range(n)]
        result = 0
        for ct in range(q):
            # print(ct, rovers, result)
            for i in range(len(rovers)):
                x, y, z = rovers[i]
                x, y = int(x), int(y)
                dr, dc = MAP[z]
                result += int(g[x][y])
                if x+dr >= 0 and x+dr < n and y+dc >= 0 and y+dc < m and \
                        g[x+dr][y+dc] != "#":
                    rovers[i] = (x+dr, y+dc, z)
                else:
                    rovers[i] = (x, y, NEXT[z])
        print(result)
