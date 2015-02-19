# Histogram Description:
# given an array of integers denoting heights of a histogram,
# return amount of water collected
# Example: 1 5 3 4 2 5 => 6
# 6    _       _
# 5   | |  _  | |
# 4   | |_| | | |
# 3   | | | |_| |
# 2  _| | | | | |
# 1 | | | | | | |
# 0


def amount_rain(arr):
    max_left = [0 for x in range(len(arr))]
    max_right = [0 for x in range(len(arr))]
    rain = 0

    tmp_max = 0

    for i in range(len(arr)):
        tmp_max = max(tmp_max, arr[i])
        max_left[i] = tmp_max

    tmp_max = 0

    for i in range(len(arr) - 1, -1, -1):
        tmp_max = max(tmp_max, arr[i])
        max_right[i] = tmp_max

    for i in range(len(arr)):
        tmp = min(max_left[i], max_right[i]) - arr[i]
        if tmp > 0:
            rain += tmp

    return rain

if __name__ == "__main__":
    num_tests = int(input())
    for test in range(num_tests):
        my_arr = [int(x) for x in raw_input().split()]
        amount = amount_rain(my_arr)
        print(amount)
