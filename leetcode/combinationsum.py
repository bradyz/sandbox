class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [[None for _ in range(len(nums)+1)] for _ in range(target+1)]
        for i in range(target+1):
            dp[i][0] = []
        for i in range(len(nums)+1):
            dp[0][i] = []
        for i in range(1, target+1):
            for j in range(1, len(nums)+1):
                if i-nums[j-1] < 0 or dp[i-nums[j-1]][j] is None:
                    continue
                if dp[i][j] is None:
                    dp[i][j] = list()
                if dp[i-nums[j-1]][j]:
                    for v in dp[i-nums[j-1]][j]:
                        dp[i][j].append(v + [nums[j-1]])
                else:
                    dp[i][j].append([nums[j-1]])
            for j in range(2, len(nums)+1):
                if dp[i][j-1] is not None:
                    if dp[i][j] is None:
                        dp[i][j] = list()
                    dp[i][j] += dp[i][j-1]
        return dp[target][len(nums)] or []
        

nums = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(nums, target))
