class Solution(object):
    def canJumpTLE(self, nums):
        dp = [False for _ in nums]
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
        return dp[-1]

    def canJump(self, nums):
        c = 0
        while c < len(nums) - 1:
            if c + nums[c] >= len(nums) - 1:
                return True
            m = 0
            x = 0
            j = c
            for i in range(c+1, min(c+nums[c]+1, len(nums))):
                if nums[i] + x > m:
                    m = nums[i] + x
                    j = i
                x += 1
            if m == 0:
                return False
            c = j
        return True


a = [2, 3, 1, 1, 4]
b = [3, 2, 1, 0, 4]
c = [0]
d = [1, 2, 0, 1]
s = Solution()
print(s.canJump(a))
print(s.canJump(b))
print(s.canJump(c))
print(s.canJump(d))
