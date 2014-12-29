def remove_dupe(arr):
    result = []
    arr.sort()

    print arr
    prev = arr[0]
    result.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] == prev:
            continue
        else:
            result.append(arr[i])
        prev = arr[i]

    return result


if __name__ == "__main__":
    with open('removedupe-input.txt', 'r') as f:
        lines = f.readlines()

    for l in lines:
        arr = [int(i) for i in l.split()]
        print arr
        print str(remove_dupe(arr))
        print "\n"
