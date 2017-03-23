import sys


DEBUG = True
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def print_grid(grid):
    for row in grid:
        print(" ".join(map(lambda char: str(char)[0], row)))


def parse(maze_string, rows):
    cols = len(maze_string) // rows
    maze = [[maze_string[i * rows + j] for j in range(cols)] for i in range(rows)]
    return maze, cols


def can_escape(x, y, maze, left, visited, rows, cols):
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return False
    elif visited[x][y]:
        return False
    elif maze[x][y] == "*":
        return False
    elif maze[x][y] == "E" and left > 0:
        return False
    elif maze[x][y] == "E" and left == 0:
        return True

    if DEBUG:
        tmp = maze[x][y]
        maze[x][y] = "!"

        print("==================================================")
        print("At:")
        print(x, y)
        print("--------------------------------------------------")
        print("Maze:")
        print_grid(maze)
        print("--------------------------------------------------")
        print("Visited:")
        print_grid(visited)

        maze[x][y] = tmp

    # Update the state.
    before = maze[x][y]

    # Hit a coin, visited is reset.
    if before == "G":
        maze[x][y] = "*"
        left -= 1

        # Reset and save visited with a fake deep copy.
        previous_visited = [list(x) for x in visited]
        visited = [[False for _ in range(cols)] for _ in range(rows)]

    visited[x][y] = True

    for dx, dy in DIR:
        if can_escape(x + dx, y + dy, maze, left, visited, rows, cols):
            return True

    # Reset the state.
    visited[x][y] = False

    if before == "G":
        visited = previous_visited
        left += 1

    maze[x][y] = before

    return False


def solve(maze, rows, cols):
    x, y = None, None
    left = 0

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == "S":
                x, y = i, j
            elif maze[i][j] == "G":
                left += 1

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    return can_escape(x, y, maze, left, visited, rows, cols)


if __name__ == "__main__":
    sys.setrecursionlimit(1000)

    tests = list()
    tests.append((5, "**G****R**ESRRG**R*G**G**"))
    tests.append((5, "**G****R**ESRRG**R****G**"))
    tests.append((3, "RSRRR**RRERR"))

    for rows, maze_string in tests:
        maze, cols = parse(maze_string, rows)

        print_grid(maze)

        result = solve(maze, rows, cols)

        print("==================================================")
        print("Solvable:", result)
