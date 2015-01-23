a = [1, [2, 3], [4, 5, [6, 7]]]
b = [[[1, 2], [3, 4]], 5, 6, [7]]


def flatten(arr):
    res = []
    for x in range(len(arr)):
        if type(arr[x]) is not list:
            res.append(arr[x])
        else:
            for el in flatten(arr[x]):
                res.append(el)
    return res

flattened = flatten(a)
print(flattened)
flattened = flatten(b)
print(flattened)
