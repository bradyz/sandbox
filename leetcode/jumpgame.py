class Solution(object):
    def canJump(self, nums):
        dp = [False for _ in nums]
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
        return dp[-1]



a = [2, 3, 1, 1, 4]
b = [3, 2, 1, 0, 4]
c = [0]
s = Solution()
print(s.canJump(a))
print(s.canJump(b))
print(s.canJump(c))
