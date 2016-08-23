class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        l = set([len(x) for x in wordDict])
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for v in l:
                if i - v < 0:
                    continue
                dp[i] |= (dp[i-v] and s[i-v:i] in wordDict)
        return dp[n]


s = "leetcode"
c = ["leet", "code"]
print(Solution().wordBreak(s, c))
