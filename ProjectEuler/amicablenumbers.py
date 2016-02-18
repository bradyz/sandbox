from math import sqrt


def divisors(y):
    yield 1
    for i in range(2, int(sqrt(y))+1):
        if y % i == 0:
            yield i
            if i != y // i:
                yield y // i


if __name__ == "__main__":
    N = 10000
    count = dict()
    for x in range(1, N):
        total = sum((y for y in divisors(x)))
        count[x] = total
    ret = 0
    keys = list(count.keys())
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            if count[keys[i]] == keys[j] and count[keys[j]] == keys[i]:
                ret += keys[i] + keys[j]
    print(ret)
