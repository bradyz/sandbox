# Maximum Bipartite Matching
# http://www.geeksforgeeks.org/maximum-bipartite-matching/

from matching import Person, adjacency


# g => graph
# u => vertex to match
# s => seen
# m => result matchings
# n => number of vertices
def bpm(g, u, s, m, n):
    for v in range(n):

        # if there exists a matching and it is not yet seen
        if g[u][v] and not s[v]:
            s[v] = True

            # if the match is not yet paired or
            # there is another matching for v's pair
            if m[v] < 0 or bpm(g, m[v], s, m, n):
                m[v] = u
                m[u] = v
                return True

    return False


# graph => adjacency matrix
# n => number of vertices
def maxBPM(graph, n):
    match = [-1 for _ in range(n)]
    result = 0

    for cur in range(n):
        seen = [False for _ in range(n)]

        if bpm(graph, cur, seen, match, n):
            result += 1

    return match


# t => total list
# m => determined matches
def print_matches(t, m):
    s = [False for _ in range(len(m))]

    for i in range(len(m)):
        if m[i] != -1 and not s[i] and not s[m[i]]:
            s[i] = True
            s[m[i]] = True
            print(str(t[i]) + " can match with " + str(t[m[i]]))


if __name__ == "__main__":
    total = [Person(*input().split()) for _ in range(int(input()))]
    pos = adjacency(total, len(total))
    matches = maxBPM(pos, len(total))
    print_matches(total, matches)
