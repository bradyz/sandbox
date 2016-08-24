def gcd(a, b):
    if a == 0 and b == 0:
        return int(1e9)
    if a == 0: 
        return b
    return gcd(b % a, a)


class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x == z or y == z or x + y == z:
            return True
        elif x + y < z:
            return False
        return (z % gcd(x, y)) == 0

x = 3
y = 5
z = 4
print(Solution().canMeasureWater(0, 0, 1))
