INF = 1e9


def slope(p1, p2):
    if p2[0] - p1[0] == 0:
        return INF
    return (p2[1] - p1[1]) / float(p2[0] - p1[0])


class Solution(object):
    def maxPoints(self, points):
        points = list(map(lambda x: (x.x, x.y), points))
        # points = list(map(tuple, points))
        n = len(points)
        m = 2
        d = dict()
        for p in points:
            d[p] = d.get(p, 0) + 1
        for i in range(n):
            slopes = [slope(points[i], points[j]) for j in range(n) if i != j]
            slopes.sort()
            c = d[points[i]]
            for i in range(1, n-1):
                if slopes[i] == slopes[i-1]:
                    c += 1
                else:
                    c = 1
                m = max(c + 1, m)
        return min(m, n)


s = Solution()
points = [[84, 250], [0, 0], [1, 0], [0, -70], [0, -70],
          [1, -1], [21, 10], [42, 90], [-42, -230]]
print(s.maxPoints(points))
