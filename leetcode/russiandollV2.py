from bisect import bisect_left


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes = set(map(tuple, envelopes))
        v = dict()
        m = dict()
        for x, y in envelopes:
            m[(x, y)] = 1
            v[x] = v.get(x, []) + [y]
        for x in v:
            v[x].sort()
        k = list(sorted(v.keys()))
        for i in range(len(k)):
            x1 = k[i]
            for y1 in v[x1]:
                for j in range(i-1, -1, -1):
                    x2 = k[j]
                    y2i = bisect_left(v[x2], y1)
                    # print(x1, y1, " ", x2, y2i, v[x2])
                    if y2i == 0:
                        continue
                    y2 = v[x2][y2i-1]
                    m[(x1, y1)] = max(m[(x1, y1)], m[(x2, y2)] + 1)
        # print(max(m.values()))
        return max(m.values() or [0])


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
s = Solution().maxEnvelopes(envelopes)
print(s)
envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
s = Solution().maxEnvelopes(envelopes)
print(s)
