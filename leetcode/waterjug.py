class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        s = [(0, 0)]
        v = set()
        while s:
            a, b = s.pop()
            if a == z or b == z or a + b == z:
                return True
            if (a, b) in v:
                continue
            v.add((a, b))
            s.append((x, b))
            s.append((a, y))
            s.append((a, 0))
            s.append((0, b))
            s.append((min(x, b + a), max(0, x - a)))
            s.append((max(0, y - b), min(y, b + a)))
        return False

x = 3
y = 5
z = 4
print(Solution().canMeasureWater(0, 0, 1))
