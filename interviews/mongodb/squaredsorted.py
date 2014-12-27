def square_elements(arr):
    minEl = 0

    for n in range(len(arr)):
        if abs(arr[n]) < abs(arr[minEl]):
            minEl = n

    x = minEl
    y = minEl + 1
    result = []

    while x >= 0 or y < len(arr):
        if abs(arr[x]) < abs(arr[y]):
            print arr[x]
            result.append(arr[x] * arr[x])
            x -= 1
        else:
            print arr[y]
            result.append(arr[y] * arr[y])
            y += 1

    return result


if __name__ == "__main__":
    with open('squaredsort-input.txt', 'r') as f:
        lines = f.readlines()

    for n in lines:
        my_arr = [int(x) for x in n.split()]
        print my_arr
        print str(square_elements(my_arr))
