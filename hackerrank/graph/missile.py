def maxBPM():
    def bpm(u):
        seen.add(u)
        for v in adj[u]:
            if v in seen:
                continue
            seen.add(v)
            if v not in match or bpm(match[v]):
                match[v] = u
                match[u] = v
                return True
        return False

    match = dict()
    result = 0
    for u in range(n):
        seen = set()
        if u not in match and bpm(u):
            result += 1
    return result


if __name__ == "__main__":
    n = int(input())
    adj = [list() for _ in range(n)]
    tf = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        t1, f1 = tf[i]
        for j in range(i+1, n):
            t2, f2 = tf[j]
            if abs(f1 - f2) <= abs(t1 - t2):
                adj[i].append(n + j)
    print(n - maxBPM())
