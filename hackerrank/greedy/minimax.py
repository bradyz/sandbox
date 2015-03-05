def minimax(a, p, q):
    minmax = 0
    a = list(set(a))
    a.sort()
    for x in range(p, q+1):
        c = bin_search(a, x)
        tmp = abs(a[c]-x)
        if c-1 >= 0:
            tmp = min(tmp, abs(a[c-1]-x))
        if c+1 < len(a):
            tmp = min(tmp, abs(a[c+1]-x))
        if tmp > minmax:
            minmax = tmp
            save = x

    return save


def bin_search(a, v):
    s = 0
    e = len(a)
    cur = -1
    while s <= e:
        h = (e+s)/2
        if h == len(a):
            return h-1
        cur = a[h]
        if v == cur:
            return h
        elif v < cur:
            e = h - 1
        else:
            s = h + 1
    return h

if __name__ == "__main__":
    size = int(input())
    arr = [int(val) for val in raw_input().split()]
    pq = [int(val) for val in raw_input().split()]
    start = pq[0]
    end = pq[1]
    print(minimax(arr, start, end))
