class Solution():
    def findLadders(self, start, end, words):
        from queue import Queue

        def graph():
            for i in range(len(words)):
                for j in range(i+1, len(words)):
                    if c(words[i], words[j]):
                        if i in g:
                            g[i].append(j)
                        else:
                            g[i] = [j]
                        if j in g:
                            g[j].append(i)
                        else:
                            g[j] = [i]

        def c(lhs, rhs):
            if len(lhs) != len(rhs):
                return False

            count = 0

            for x, y in zip(lhs, rhs):
                count += (x != y)

            return (count <= 1)

        def path_length(parent, b, e):
            count = 1
            while e != b:
                e = parent[e]
                count += 1
            return count

        def bfs():
            q = Queue()
            p = {}
            idx = words.index(start)
            q.put(idx)
            p[idx] = -1

            while not q.empty():
                cur = q.get()

                if words[cur] == end:
                    return path_length(p, words.index(start), words.index(end))

                for v in filter(lambda x: x not in p, g[cur]):
                    p[v] = cur
                    q.put(v)

            return 0

        words = words + [start] + [end]
        g = {}
        graph()

        return bfs()


if __name__ == "__main__":
    dictionary = ["hot", "dot", "dog", "lot", "log"]

    start = "hit"
    end = "cog"

    s = Solution()
    print(s.findLadders(start, end, dictionary))
