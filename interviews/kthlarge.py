def kthLargeSort(arr, n):
    arr.sort()
    print arr
    a = len(arr) - n
    prev = 0
    for x in reversed(arr):
        if prev != x:
            print prev, x
            a -= 1
            if a == 0:
                return x
        prev = x
    return ""

if __name__ == "__main__":
    with open('kthlarge-input.txt') as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        if idx % 2 == 0:
            x = [int(i) for i in line.split()]
        else:
            k = int(line)
            print x, k
            print kthLargeSort(x, k)
