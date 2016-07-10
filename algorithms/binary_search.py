def binary_search_left(a, can):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if can(a[mid]):
            lo = mid+1
        else:
            hi = mid
    return lo


a = [0, 0, 0, 1]

# the number of things that satisfy the constraint
print(binary_search_left(a, lambda x: x < 0))
print(binary_search_left(a, lambda x: x < 1))
