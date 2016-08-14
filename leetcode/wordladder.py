from Queue import Queue


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.add(endWord)
        wordList.add(beginWord)
        q = Queue()
        q.put((beginWord, 1))
        wordList.remove(beginWord)
        while not q.empty():
            u, c = q.get()
            if u == endWord:
                return c
            for k in range(len(u)):
                tmp = list(u)
                for j in "abcdefghijklmnopqrstuvwxyz":
                    tmp[k] = j
                    v = "".join(tmp)
                    if v in wordList:
                        q.put((v, c + 1))
                        wordList.remove(v)
        return 0


s = Solution()
beginWord = "lost"
endWord = "miss"
wordList = set(["most", "mist", "miss", "lost", "fist", "fish"])
print(s.ladderLength(beginWord, endWord, wordList))
