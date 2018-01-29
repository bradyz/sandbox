def hash(tx, s):
    left_right = list()

    for i in range(len(tx)):
        x = int(tx[i])
        y = int(s[i % len(s)])
        if y == 0:
            left_right.append(x)
        elif x == 0:
            left_right.append(y)
        else:
            left_right.append(x % y)
    return left_right


def lead_zeros(x):
    result = 0

    for i in range(len(x)):
        result += x[i] == 0

        if x[i] != 0:
            break

    return result


tx, n, s = input().split()


x = int(tx)

while True:
    if lead_zeros(hash(str(x), s)) >= int(n):
        break
    x += 1

print(x - int(tx))
