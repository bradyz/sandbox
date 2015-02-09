import sys


def collatz(low, high):
    def col(num):
        if num != 1:
            if num % 2 == 0:
                count = col(num/2) + 1
            else:
                count = col(3*num+1) + 1
            cache[num] = count
            return count
        else:
            return 1
    cache = {}
    cache[1] = 1
    max_val = 0

    if low > high:
        low, high = high, low

    for x in range(low, high + 1):
        tmp = col(x)
        if tmp > max_val:
            max_val = tmp

    return max_val

if __name__ == "__main__":
    for line in sys.stdin:
        args = line.split()
        lower = int(args[0])
        upper = int(args[1])
        num = collatz(lower, upper)
        print(str(lower) + " " + str(upper) + " " + str(num))
