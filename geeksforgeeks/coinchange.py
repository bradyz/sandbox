inf = 1000000

def optimal(i, val):
    if val < 0:
        return inf
    if i <= 0:
        return inf
    if val == 0:
        return 0

    res = inf
    res = min(res, optimal(i, val-coins[i]))
    res = min(res, optimal(i-1, val))

    return res

if __name__ == "__main__":
    num_tests = int(input())

    for test in range(num_tests):
        coins = [int(val) for val in raw_input().split()]
        value = int(input())
        num = optimal(len(coins)-1, value)
        print(num)
