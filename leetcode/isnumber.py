class Solution(object):
    def isNumber(self, s):
        if len(s.split()) > 1:
            return False

        for t in (int, float, complex):
            try:
                t(s)
                return True
            except:
                pass

        return False

if __name__ == "__main__":
    s = Solution()
    print(s.isNumber("+ 1"))
