class Solution(object):
    def kthSmallest(self, matrix, k):
        return sorted(y for x in matrix for y in x)[k-1]


matrix = [[1,  5,  9],
          [10, 11, 13],
          [12, 13, 15]]
k = 8
print(Solution().kthSmallest(matrix, k))
