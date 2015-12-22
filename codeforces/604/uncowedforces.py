p = [500, 1000, 1500, 2000, 2500]
m = list(map(int, input().split()))
w = list(map(int, input().split()))
h = list(map(int, input().split()))
res = 0
for xi, mi, wi in zip(p, m, w):
    tmp = max(0.3 * xi, (1 - mi / 250) * xi - 50 * wi)
    res += tmp
res += h[0] * 100 - h[1] * 50
print(int(res))
