from sys import maxsize as MAXINT


# k => key array (cost of connecting)
# m => mst array (is it already included)
def min_key(k, m):
    m_v = MAXINT
    m_i = -1

    for i in range(len(k)):
        if not m[i] and k[i] < m_v:
            m_i = i
            m_v = k[i]

    print("min: " + str(m_i))
    return m_i


def prim(g, p, n):
    m = [[None for j in range(n)] for i in range(n)]
    mst = [False for _ in range(n)]
    key = [MAXINT for _ in range(n)]
    parent = [None for _ in range(n)]

    key[0] = 0                  # make sure the first vertex is picked
    parent[0] = -1              # first node is root of MST

    # turn the graph into a matrix
    for e in g:
        m[e.a.v][e.b.v] = m[e.b.v][e.a.v] = e

    for i in range(n):
        u = min_key(key, mst)
        mst[u] = True
        for v in range(n):
            if not mst[v] and m[u][v] and m[u][v].w < key[u]:
                parent[v] = u
                key[v] = m[u][v].w
                print(parent, key)

    for i in range(n):
        print(str(i) + " " + str(parent[i]))
