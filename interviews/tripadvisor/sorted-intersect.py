from collections import Counter


def intersect(a, b):
    b_c = Counter()
    res = []

    for x in b:
        b_c[x] += 1

    for val in a:
        if b_c[val] > 0:
            res.append(val)

    return res

if __name__ == "__main__":
    a_arr = [2, 3, 4, 5]
    b_arr = [2, 4, 8, 9]    # => [2,4]
    result = intersect(a_arr, b_arr)
    print(result)
