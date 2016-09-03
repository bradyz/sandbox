class Solution(object):
    def jump(self, nums):
        c = 0
        r = 0
        while c < len(nums) - 1:
            m = 0
            x = 0
            for i in range(c+1, min(c+nums[c]+1, len(nums))):
                if nums[i] + x >= m or i == len(nums) - 1:
                    m = nums[i] + x
                    c = i
                x += 1
            r += 1
        return r


a = [2, 3, 1, 1, 4]
print(Solution().jump(a))
a = [2, 3, 1]
print(Solution().jump(a))
a = [1, 2, 0, 1]
print(Solution().jump(a))
