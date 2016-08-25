def foo(s):
    if not s:
        return s
    n = len(s)
    best = [0 for _ in range(n)]
    for i in range(n):
        jm = 0
        for j in range(1, n):
            if i - j < 0 or i + j >= n:
                break
            elif s[i-j] != s[i+j]:
                break
            jm = max(jm, j)
        best[i] = jm
    x = 0
    for i in range(n):
        if best[i] == i:
            x = i
    return s[x + best[x] + 1:][::-1] + s


def bar(s):
    if not s:
        return s
    n = len(s)
    best = [0 for _ in range(n)]
    for i in range(n):
        jm = 0
        for j in range(n):
            if i - j - 1 < 0 or i + j >= n:
                break
            elif s[i-j-1] != s[i+j]:
                break
            jm = max(jm, j + 1)
        best[i] = jm
    x = 0
    for i in range(n):
        if best[i] == i:
            x = i
    return s[x + best[x]:][::-1] + s


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = []
        r.append(foo(s))
        r.append(foo("".join(reversed(s))))
        r.append(bar(s))
        r.append(bar("".join(reversed(s))))
        return min(r, key=lambda x: len(x))


s = "abb"
print(Solution().shortestPalindrome(s))
