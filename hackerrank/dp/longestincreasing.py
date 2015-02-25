import sys


def longest_inc(arr):
    dp = [[arr[0]]]
    max_yet = []
    print(arr)
    print(dp)
    for i, val in enumerate(arr):
        if i > 0:
            m = 0
            v = []
            for j in range(i):
                if len(dp[j]) >= m and arr[j] <= val:
                    m = len(dp[j])
                    v = dp[j]
            dp.append(v + [val])
        print(dp)
        if len(dp[i]) > len(max_yet):
            max_yet = dp[i]
    print(max_yet)
    return max_yet


def long_inc(arr):
    dp = [1 for _ in range(len(arr))]
    max_yet = 0
    for i in range(1, len(arr)):
        m = 1
        for j in range(i):
            if dp[j] > m and arr[j] < arr[i]:
                m = dp[j]
        dp[i] = m + 1
        print(dp)
        max_yet = max(max_yet, dp[i])
    return max_yet


def long_nlogn(arr):
    m = [0 for _ in range(len(arr)+1)]
    L = 0
    # print(arr)

    for i in range(len(arr)):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo+hi)/2
            if arr[m[mid]] < arr[i]:
                lo = mid+1
            else:
                hi = mid-1
        newL = lo

        m[newL] = i
        L = max(L, newL)
        # print("I: " + str(i) + " Val: " + str(arr[i]))
        # print("M: " + str(m))

    return L


if __name__ == "__main__":
    my_arr = []
    for i, line in enumerate(sys.stdin):
        if i > 0:
            my_arr.append(int(line))
    num = long_nlogn(my_arr)
    print(num)
