from queue import Queue


def close(lhs, rhs):
    if len(lhs) != len(rhs):
        return False

    count = 0

    for x, y in zip(lhs, rhs):
        count += (x != y)

    return (count <= 1)


def bfs(start, target, words):
    q = Queue()
    q.put([start, [start]])

    while not q.empty():
        cur, vis = q.get()

        if cur == target:
            return vis

        for val in filter(lambda x: x not in vis and close(cur, x), words):
            q.put([val, vis + [val]])

    return []

if __name__ == "__main__":
    num_words = int(input())
    dictionary = [input() for _ in range(num_words)]

    start = "TOON"
    end = "PLEA"

    print(bfs(start, end, dictionary))
