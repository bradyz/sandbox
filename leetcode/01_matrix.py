from collections import deque


def bfs(x, y, matrix, m, n):
    queue = deque()

    queue.append((x, y, 0))
    visited = set([(x, y)])

    while len(queue) > 0:
        cx, cy, cw = queue.popleft()

        if matrix[cx][cy] == 0:
            return cw

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if nx < 0 or nx >= m:
                continue
            elif ny < 0 or ny >= n:
                continue
            elif (nx, ny) in visited:
                continue

            queue.append((nx, ny, cw + 1))
            visited.add((nx, ny))

    return -1


class Solution(object):
    def updateMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        answers = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                answers[i][j] = bfs(i, j, matrix, m, n)

        return answers
