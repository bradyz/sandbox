from math import ceil


def chief_hopper(arr):
    m = 0

    for i in range(len(arr)-1):
        tmp = ceil((arr[i] + arr[i+1]) / 2)
        if tmp > m:
            m = tmp

    if m > 0:
        m -= arr[len(arr)-1]

    for i in range(len(arr), 0, -1):
        m = ceil((m + arr[i-1]) / 2)

    print(m)

if __name__ == "__main__":
    a = int(input())
    b = [int(v) for v in input().split()]
    chief_hopper(b)
