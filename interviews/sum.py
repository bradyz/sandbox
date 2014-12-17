def hasPair(arr, n):
    for x in arr:
        for y in arr:
            if x != y and x + y == n:
                return str(x) + " " + str(y)
    return ""


def hasPairSort(arr, n):
    arr.sort()
    x = len(arr) / 2
    y = len(arr) / 2 + 1
    while y >= 0:
        while x < len(arr):
            s = arr[x] + arr[y]
            if s == n:
                return str(arr[x]) + " " + str(arr[y])
            else:
                if s > n:
                    y -= 1
                else:
                    x += 1
    return ""


def hasPairDict(arr, n):
    d = dict()
    for x in arr:
        d[x] = n - x
    for x in d:
        if d.get(x) in arr:
            return str(d.get(x)) + " " + str(x)
    return ""


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        if idx % 2 == 0:
            x = [int(i) for i in line.split()]
        else:
            pair = int(line)
            print x, pair
            print "O(n^2)\t" + hasPair(x, pair)
            print "O(nlogn)\t" + hasPairSort(x, pair)
            print "O(n)\t" + hasPairDict(x, pair)
