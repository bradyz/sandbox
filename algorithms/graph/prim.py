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

    return m_i


# x => node
# y => parent of node
# z => edge
def belongs_to(x, y, z):
    return (z.a.v == x and z.b.v == y) or (z.a.v == y and z.b.v == x)


def prim(g, p, n):
    m = [[None for j in range(n)] for i in range(n)]
    mst = [False for _ in range(n)]
    key = [MAXINT for _ in range(n)]
    parent = [None for _ in range(n)]
    r = []

    key[0] = 0                  # make sure the first vertex is picked
    parent[0] = -1              # first node is root of MST

    # turn the graph into a matrix
    for e in g:
        m[e.a.v][e.b.v] = m[e.b.v][e.a.v] = e

    # look for the minimum edge to add
    for i in range(n):
        u = min_key(key, mst)   # find minimum node to add
        mst[u] = True           # add point to mst set

        # expand the cut
        for v in range(n):
            if not mst[v] and m[u][v] and m[u][v].w < key[v]:
                parent[v] = u
                key[v] = m[u][v].w

    for i in range(1, n):
        for e in g:
            if belongs_to(i, parent[i], e):
                r.append(e)

    return r
