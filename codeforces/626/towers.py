n, m = map(int, input().split())
mx = m * 3
nx = mx // 6 * 2 + n * 2
ny = n * 2
my = ny // 6 * 3 + m * 3
print(min(max(nx, mx), max(ny, my)))
