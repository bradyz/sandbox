from collections import Counter


def remove_dupe(arr):
    result = []
    arr.sort()
    prev = arr[0]
    result.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] == prev:
            continue
        else:
            result.append(arr[i])
        prev = arr[i]

    return result


def remove_dupe_map(arr):
    count = Counter()

    for n in arr:
        count[n] += 1

    return count.keys()


if __name__ == "__main__":
    with open('removedupe-input.txt', 'r') as f:
        lines = f.readlines()

    for l in lines:
        arr = [int(i) for i in l.split()]
        print "Arr: " + str(arr)
        print "Map Method: " + str(remove_dupe_map(arr))
        print "Sort Method: " + str(remove_dupe(arr))
        print ""
