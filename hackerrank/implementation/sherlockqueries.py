import sys


def a_elements(a, b, c, m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if j % b[i] == 0:
                a[j] = a[j] * c[i]

    for i in range(1, n + 1):
        a[i] = a[i] % 1000000007

    return a


def a_fast(a, b, c, m, n):
    max_mn = max([m, n])
    count = [-1] * (max_mn + 1)

    for x in range(1, m + 1):
        if count[b[x]] == -1:
            count[b[x]] = c[x]
        else:
            count[b[x]] = (count[b[x]] * c[x]) % 1000000007

    for x in range(1, n + 1):
        for y in range(1, n / x + 1):
            if count[x] != -1:
                a[x * y] = (a[x * y] * count[x])

    for i in range(1, n + 1):
        a[i] = a[i] % 1000000007

    return a


def arr_shifted(my_arr):
    tmp_arr = [None] * (len(my_arr) + 1)

    for x in range(1, len(tmp_arr)):
        tmp_arr[x] = my_arr[x - 1]

    return tmp_arr

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            parsed = [int(x) for x in line.split()]
            a_size = parsed[1]
            b_size = parsed[0]
        elif i == 1:
            a_arr = arr_shifted([int(x) for x in line.split()])
        elif i == 2:
            b_arr = arr_shifted([int(x) for x in line.split()])
        elif i == 3:
            res = ""
            c_arr = arr_shifted([int(x) for x in line.split()])
            # a_res = a_elements(a_arr, b_arr, c_arr, a_size, b_size)
            a_res = a_fast(a_arr, b_arr, c_arr, a_size, b_size)
            for x in range(len(a_res)):
                if x > 0:
                    res += str(a_res[x]) + " "
            print(res)
