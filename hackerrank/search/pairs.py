def pairs_diff(arr, d):
    distinct = set(arr)
    pairs = 0

    for val in arr:
        if val + d in distinct:
            pairs += 1
        if val - d in distinct:
            pairs += 1

    return pairs / 2

if __name__ == "__main__":
    args = [int(x) for x in raw_input().split()]
    size = args[0]
    diff = args[1]
    my_arr = [int(x) for x in raw_input().split()]
    num_pairs = pairs_diff(my_arr, diff)
    print(num_pairs)
