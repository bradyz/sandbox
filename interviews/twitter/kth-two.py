def kth_large(a, b, k):
    ai = 1
    bi = 1

    while ai > 0 or bi > 0:
        if ai < len(a) and a[-ai] > b[-bi]:
            if ai + bi - 1 == k:
                return a[-ai]
            ai += 1
        else:
            if ai + bi - 1 == k:
                return b[-bi]
            bi += 1

if __name__ == "__main__":
    a_arr = [1]
    b_arr = [0, 2, 4, 6, 8]
    result = kth_large(a_arr, b_arr, 3)
    print(a_arr)
    print(b_arr)
    print(sorted(a_arr+b_arr))
    print("3rd Largest: " + str(result))

    a_arr = [1, 3, 5, 7, 9]
    b_arr = [0, 2, 4, 6, 8]
    result = kth_large(a_arr, b_arr, 3)
    print(a_arr)
    print(b_arr)
    print(sorted(a_arr+b_arr))
    print("3rd Largest: " + str(result))
