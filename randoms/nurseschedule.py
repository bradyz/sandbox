from random import randrange


def powerset(c, d=[]):
    yield d
    for i in range(len(c)):
        for s in powerset(c[i+1:], d + [c[i]]):
            yield s


def valid(c, d):
    for y in d:
        overlap = False
        for x in c:
            overlap |= (x[0] < y[1] and y[0] < x[1])
        if not overlap:
            return False

    for i in range(len(c)):
        for j in range(i+1, len(c)):
            if c[i][0] <= c[j][1] and c[j][0] <= c[i][1]:
                return False

    return True


def brute_force(t):
    m = None

    for e in powerset(t):
        if valid(e, set(t) - set(e)) and (not m or len(e) < len(m)):
            m = e

    print(" ".join(map(str, m)))


def algorithm(times):
    edges = {nurse: set() for nurse in times}
    seen = set()
    committee = set()

    for i in range(len(times)):
        for j in range(i+1, len(times)):
            if times[i][0] <= times[j][1] and times[j][0] <= times[i][1]:
                edges[times[i]].add(times[j])
                edges[times[j]].add(times[i])

    while set(times) - seen:
        max_nurse = (-1, -1)
        max_neighbors = 0

        for nurse in edges:
            not_seen = edges[nurse] - seen

            if len(not_seen) > max_neighbors:
                max_neighbors = len(not_seen)
                max_nurse = nurse

        if max_neighbors <= 0:
            max_nurse = list(set(times)-seen)[0]

        committee.add(max_nurse)
        seen.add(max_nurse)

        for neighbor in edges[max_nurse]:
            seen.add(neighbor)

    print(" ".join(map(str, committee)))


if __name__ == "__main__":
    n = 10
    k = 1000

    v = [tuple(sorted((randrange(k), randrange(k)))) for _ in range(n)]
    # v = [tuple(map(int, input().split())) for _ in range(n)]

    print(v)
    brute_force(v)
    algorithm(v)
