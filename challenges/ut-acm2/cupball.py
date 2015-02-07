num_test = int(input())

for test in range(num_test):
    args = raw_input()
    args = [int(x) for x in args.split()]
    cups = args[0]
    swaps = args[1]
    arr = [None for x in range(cups)]
    arr[0] = 1
    for swap in range(swaps):
        parsed = raw_input()
        parsed = [int(x) for x in parsed.split()]
        a = parsed[0]
        b = parsed[1]
        arr[a], arr[b] = arr[b], arr[a]
    print(arr.index(1))
