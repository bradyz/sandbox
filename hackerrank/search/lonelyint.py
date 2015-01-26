from collections import Counter


def lonelyinteger(a):
    count = Counter()

    for x in a:
        count[x] += 1

    for x in count:
        if count[x] == 1:
            return x

    return -1

if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
