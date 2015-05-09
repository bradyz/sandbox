import sys

# Find the maximum weighted path to a leaf
#         1
#        / \
#       6   4
#      / \ / \
#     8   9   3
#    / \ / \ / \
#   9  12   6   7


# index of current element
# num of total elements
def child(idx, total):
    num = idx
    level = 1

    # slow but its right
    while idx - level >= 0:
        idx -= level
        level += 1

    if num + level < total:
        return num + level, num + level + 1
    else:
        return -1, -1


def max_val(v, n):
    def dfs(c_i, cur):
        if c[c_i] < cur + v[c_i]:
            c[c_i] = cur + v[c_i]
            for i in child(c_i, n):
                if i != -1:
                    dfs(i, c[c_i])

    c = [-1 for _ in range(n)]         # cumulative sums
    dfs(0, 0)
    print(c)


def solve(v, n):
    dp = [[-1 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(len(v[i])):
            if i == 0 and j == 0:
                dp[i][j] = v[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + v[i][j]
            elif j == len(v[i]):
                dp[i][j] = dp[i-1][j-1] + v[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + v[i][j]

    print(max(dp[n-1]))


if __name__ == "__main__":
    values = []
    i = 0

    for line in sys.stdin:
        i += 1
        values.append(list(map(int, line.split())))

    solve(values, i)
