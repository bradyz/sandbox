def kth_large(a, b, k):
    ai = len(a) - 1
    bi = len(b) - 1

    while ai > 0 and bi > 0:
        if a[ai] > b[bi]:
            ai -= 1
            if len(a)-ai+len(b)-bi == k:
                return a[ai]
        else:
            bi -= 1
            if len(a)-ai+len(b)-bi == k:
                return b[bi]

if __name__ == "__main__":
    a_arr = [1, 3, 5, 7, 9]
    b_arr = [0, 2, 4, 6, 8]
    result = kth_large(a_arr, b_arr, 3)
    print(a_arr)
    print(b_arr)
    print(sorted(a_arr+b_arr))
    print("3rd Largest")
    print(result)
