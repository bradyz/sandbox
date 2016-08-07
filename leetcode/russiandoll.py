class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort()
        n = len(envelopes)
        can = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                can[i][j] = (envelopes[i][0] > envelopes[j][0] and
                             envelopes[i][1] > envelopes[j][1])
        m = [1 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if can[i][j]:
                    m[i] = max(m[i], m[j] + 1)
        return max(m or [0])


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
s = Solution().maxEnvelopes(envelopes)
print(s)
envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
s = Solution().maxEnvelopes(envelopes)
print(s)
