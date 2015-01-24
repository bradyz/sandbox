import sys


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

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            num_cases = int(line.strip("\n"))
        elif i % 2 == 0:
            parsed = [int(x) for x in line.split()]
            print(num_shifts(parsed))
