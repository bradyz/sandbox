import sys


def collatz(low, high):
    cache = {}
    cached = set()
    max_val = 0
    if low > high:
        low, high = high, low

    for x in range(low, high + 1):
        count = 1
        tmp = x
        contain = [tmp]

        while(tmp != 1):
            if tmp in cached:
                count += cache[tmp] - 1
                tmp = 1
            else:
                if tmp % 2 == 0:
                    tmp /= 2
                else:
                    tmp = 3 * tmp + 1
                contain.append(tmp)
                count += 1

        if count > max_val:
            max_val = count

        for y in range(len(contain)):
            if contain[y] not in cached:
                cached.add(contain[y])
                cache[contain[y]] = count - y

    return max_val

if __name__ == "__main__":
    for line in sys.stdin:
        args = line.split()
        lower = int(args[0])
        upper = int(args[1])
        num = collatz(lower, upper)
        print(str(lower) + " " + str(upper) + " " + str(num))
