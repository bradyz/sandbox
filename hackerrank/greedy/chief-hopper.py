from math import ceil


def chief_hopper(arr):
    m = 0
    mi = 0
    for i in range(len(arr)-1):
        if ceil((arr[i]+arr[i+1])/2) > m:
            mi = i
            m = max(ceil((arr[i]+arr[i+1])/2), m)
    for i in range(mi, 0, -1):
        m = ceil((m + arr[i-1]) / 2)
    print(m)

if __name__ == "__main__":
    a = int(input())
    b = [int(v) for v in input().split()]
    chief_hopper(b)
