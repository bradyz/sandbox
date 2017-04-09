import heapq


def solve(grid, n, m, k):
    left = [[0 for _ in range(m)] for _ in range(n)]
    left[0][0] = k

    queue = [(0, 0)]

    result = 0

    while queue:
        x, y = heapq.heappop(queue)

        if x == n - 1 and y == m - 1:
            result += left[x][y]
            left[x][y] = 0
            continue
        elif left[x][y] == 0:
            continue

        c = left[x][y]
        down_free = (x + 1 < n and grid[x+1][y] == ".")
        right_free = (y + 1 < m and grid[x][y+1] == ".")

        if down_free and right_free:
            heapq.heappush(queue, (x+1, y))
            heapq.heappush(queue, (x, y+1))
            left[x+1][y] += int(c / 2 + 0.5)
            left[x][y+1] += int(c / 2)
        elif down_free:
            heapq.heappush(queue, (x+1, y))
            left[x+1][y] += c
        elif right_free:
            heapq.heappush(queue, (x, y+1))
            left[x][y+1] += c

        left[x][y] = 0

    return result


n, m, k = map(int, input().split())
grid = [input() for _ in range(n)]
print(solve(grid, n, m, k))
