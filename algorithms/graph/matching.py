from pprint import PrettyPrinter
pp = PrettyPrinter()


class Person:
    def __init__(self, name, team, office):
        self.info = [0 for _ in range(3)]
        self.info[0] = name
        self.info[1] = team
        self.info[2] = office

    def __getitem__(self, i):
        return self.info[i]


def similar(a, b):
    return a[0] == b[0] or a[1] == b[1] or a[2] == b[2]


# c => list of people
# n => length of list
def adjacency(c, n):
    r = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and not similar(c[i], c[j]):
                r[i][j] = 1
    return r


# c => list of people
# g => adjacency graph
# n => length of list
def greedy(c, g, n):
    # result of matching pairs
    r = []
    stop = False

    while not stop:
        m_i = -1
        m_c = n
        stop = True

        # find the minimum nonzero amount
        for i in range(n):
            tmp = g[i].count(1)
            if tmp < m_c and tmp > 0:
                m_i = i
                m_c = tmp

        if m_i != n:
            # look for least match
            p_i = -1
            p_c = n
            for i in [j for j in range(n) if g[m_i][j]]:
                tmp = g[i].count(1)
                if tmp < p_c and tmp > 0:
                    p_i = i
                    p_c = tmp
            if p_c != n:
                r.append((m_i, p_i))
                for i in range(n):
                    g[p_i][i] = 0
                    g[m_i][i] = 0
                stop = False

    return r


if __name__ == "__main__":
    total = [Person(*input().split()) for _ in range(int(input()))]
    pos = adjacency(total, len(total))
    greed = greedy(total, pos, len(total))
