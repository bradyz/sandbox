DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(i, j, matrix, m, n, seen):
    seen.add((i, j))

    for di, dj in DIR:
        ni = i + di
        nj = j + dj

        if (ni, nj) in seen:
            continue
        elif ni < 0 or ni >= m or nj < 0 or nj >= n:
            continue
        elif matrix[i][j] > matrix[ni][nj]:
            continue

        dfs(i + di, j + dj, matrix, m, n, seen)


class Solution(object):
    def pacificAtlantic(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return list()

        m = len(matrix)
        n = len(matrix[0])

        s_seen = set()
        t_seen = set()

        for i in range(m):
            dfs(i, 0, matrix, m, n, s_seen)
            dfs(i, n-1, matrix, m, n, t_seen)

        for i in range(n):
            dfs(0, i, matrix, m, n, s_seen)
            dfs(m-1, i, matrix, m, n, t_seen)

        result = list()

        for i in range(m):
            for j in range(n):
                if (i, j) not in s_seen:
                    continue
                elif (i, j) not in t_seen:
                    continue

                result.append((i, j))

        return result


if __name__ == '__main__':
    m, n = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(m)]

    print(Solution().pacificAtlantic(matrix))
