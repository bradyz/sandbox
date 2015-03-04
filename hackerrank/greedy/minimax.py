from collections import Counter


def minimax(a, p, q):
    minmax = 0
    save = 0
    a = list(set(a))
    count = {}
    for v in a:
        count[v] = 1
    for x in range(p, q+1):
        i = 0
        while x+i not in count and x-1 not in count:
            i += 1
        if i > minmax:
            minmax = i
            save = x
    return save

if __name__ == "__main__":
    size = int(input())
    arr = [val for val in raw_input().split()]
    arr = map(int, arr)
    pq = [int(val) for val in raw_input().split()]
    start = pq[0]
    end = pq[1]
    print(minimax(arr, start, end))
