class Solution(object):
    def minWindow(self, s, t):
        n = len(s)
        c = dict()
        for v in t:
            c[v] = c.get(v, 0) + 1
        x = set(t)
        h = {z: 0 for z in s}
        r = s + "X"
        i, j = 0, 0
        while i < len(s) and j <= len(s):
            if not x:
                h[s[i]] -= 1
                if h[s[i]] < c.get(s[i], 0):
                    x.add(s[i])
                i += 1
            elif j == n:
                break
            else:
                h[s[j]] += 1
                if s[j] in x and h[s[j]] == c[s[j]]:
                    x.remove(s[j])
                j += 1
            if not x and j - i < len(r):
                r = s[i:j]
        if len(r) > len(s):
            return ""
        return r


s = Solution()
S = "ab"
T = "a"
print(s.minWindow(S, T))
