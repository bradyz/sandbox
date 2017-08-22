class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return list()

        x1 = 1
        x2 = 2
        c1 = 0
        c2 = 0

        for x in nums:
            if x == x1:
                c1 += 1
            elif x == x2:
                c2 += 1
            elif c1 == 0:
                x1 = x
                c1 = 1
            elif c2 == 0:
                x2 = x
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        result = list()

        for x in [x1, x2]:
            if nums.count(x) > len(nums) // 3:
                result.append(x)

        return result


if __name__ == '__main__':
    s = Solution()

    test_1 = [1, 1, 1, 0, 0, 0, 0, 0, 0]
    test_2 = [1, 1, 1, 1, 2, 2, 2, 2, 2]
    test_3 = [1, 1, 1, 2, 2, 2]
    test_4 = [1, 2, 3, 4, 5]
    test_5 = [2, 2, 1, 3]
    test_6 = [0, 3, 4, 0]

    print(s.majorityElement(test_1))
    print(s.majorityElement(test_2))
    print(s.majorityElement(test_3))
    print(s.majorityElement(test_4))
    print(s.majorityElement(test_5))
    print(s.majorityElement(test_6))
