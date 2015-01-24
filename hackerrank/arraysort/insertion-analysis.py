import sys


def shifts(arr):
    count = 0
    for x in range(len(arr)):
        for y in range(x):
            if arr[x] < arr[y]:
                count += 1
    return count


def num_shifts(arr):
    arr_sorted = sorted(arr)
    count = 0
    used = [False] * len(arr)

    for x in range(len(arr)):
        indices = [i for i, el in enumerate(arr_sorted) if el == arr[x]]
        print(arr[x], indices)
        for i in indices:
            if not used[i]:
                count += abs(x - i)
                used[i] = True
                break

    return count / 2


count = 0


def msort3(x):
    global count
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = msort3(x[:mid])
    z = msort3(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            count += len(y) - i
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            num_cases = int(line.strip("\n"))
        elif i % 2 == 0:
            parsed = [int(x) for x in line.split()]
            arr = msort3(parsed)
            print(count)
            count = 0
            # print(shifts(parsed))
