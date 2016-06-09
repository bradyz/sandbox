n = int(input())
k = int(input())
c = [int(input()) for _ in range(n)]
c.sort()
p = c[::]
for i in range(1, n):
    p[i] += p[i-1]
# print(c)
# print(p)
m = 1e9
for j in range(n - k + 1):
    total = 0
    for i in range(k-1):
        total += (p[k-1+j] - p[i+j]) - (c[i+j] * (k - i - 1))
    # print(total)
    m = min(m, total)
print(m)
# for x in range(k-1, n):
#     r = 0
#     for i in range(x - k + 1, x + 1):
#         for j in range(i + 1, x + 1):
#             r += abs(c[i] - c[j])
#     m = min(m, r)
#     print(c[x] - c[x-k+1], r)
# print(m)
