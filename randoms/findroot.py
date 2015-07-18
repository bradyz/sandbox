# Find the root in O(n) time and O(1) space
#    3
#   / \
#  2   4
#     / \
#    1   5
c = {1: [], 2: [], 3: [2, 4], 4: [1, 5], 5: []}
n = len(c)


def solve():
    global c, n
    t = n * (n+1) // 2
    for u in c:
        for v in c[u]:
            t -= v
    print(t)

solve()
