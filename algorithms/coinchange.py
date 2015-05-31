inf = 1000000
mem = {}


def optimal(i, val):
    if val < 0:
        return inf
    if val == 0:
        return 0
    if i < 0:
        return inf

    if str((i, val)) in mem:
        return mem[(str((i, val)))]

    res = inf
    res = min(res, 1 + optimal(i, val-coins[i]))
    res = min(res, optimal(i-1, val))

    mem[str((i, val))] = res

    return res

if __name__ == "__main__":
    num_tests = int(input())

    for test in range(num_tests):
        coins = [int(val) for val in raw_input().split()]
        value = int(input())
        num = optimal(len(coins)-1, value)
        print(num)
