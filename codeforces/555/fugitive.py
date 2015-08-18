from bisect import bisect_left as bisect

n, m = map(int, input().split())
c = list(tuple(map(int, input().split())) for _ in range(n))
d = list(tuple(map(int, input().split())))

print(c, d)
# for j in range(n-1):
#     i = v[j][0]
#     print(i)
#     f = False
#     s = bisect(d, c[i][0]-c[i-1][1])
#     t = bisect(d, c[i][1]-c[i-1][0])
#     for k in range(s, t+1):
#         if not u[k]:
#             u[k] = True
#             f = True
#             r.append((k, x[j][1]))
#             break
#     if not f:
#         r = list()
#         break
#
# print(r)
