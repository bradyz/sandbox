def dfs(u, g, vis, order):
    if u in vis:
        return
    vis.add(u)
    for v in g.get(u, []):
        dfs(v, g, vis, order)
    order.append(u)


def kosajaru(g):
    # reversed order of completion.
    first_vis = set()
    first_order = list()
    for u in g:
        dfs(u, g, first_vis, first_order)
    first_order = list(reversed(first_order))

    # g with edges reversed.
    g_reversed = dict()
    for u in g:
        for v in g.get(u, []):
            if v not in g_reversed:
                g_reversed[v] = list()
            g_reversed[v].append(u)

    # dfs in reverse order, will find sccs.
    second_vis = set()
    sccs = list()
    for u in first_order:
        scc = list()
        dfs(u, g_reversed, second_vis, scc)
        if scc:
            sccs.append(scc)

    return sccs


if __name__ == "__main__":
    g = dict()
    for _ in range(int(input())):
        u, v = map(int, input().split())
        if u not in g:
            g[u] = list()
        g[u].append(v)

    print(kosajaru(g))
