def cycle(d):
    seen = dict()

    current = 0
    x = 1

    while True:
        remainder = x % d

        if remainder == 0:
            return 0
        elif remainder in seen:
            return current - seen[remainder]

        seen[remainder] = current
        current += 1
        x = 10 * remainder

    return -1


result_i = 0
result_cycle = 0

for i in range(1, 1001):
    print("1/%d, %d" % (i, cycle(i)))

    if cycle(i) > result_cycle:
        result_i = i
        result_cycle = cycle(i)

print(result_i, result_cycle)
