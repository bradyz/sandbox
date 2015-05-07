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
        c[c_i] = max(c[c_i], cur + v[c_i])
        for i in child(c_i, n):
            if i != -1:
                dfs(i, c[c_i])

    c = [-1 for _ in range(n)]         # cumulative sums
    dfs(0, 0)
    print(c)


if __name__ == "__main__":
    values = [1, 6, 4, 8, 9, 3, 9, 12, 6, 7]
    max_val(values, len(values))
