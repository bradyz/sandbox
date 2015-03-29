def cipher(c, l, k):
    res = [False for _ in range(l)]
    res[0] = c[0]
    for i in range(1, l):
        tmp = c[i]
        for j in range(min(k-1, len(res))):
            tmp ^= res[i-j-1]
        res[i] = tmp

    print("".join(list(map(lambda x: str(int(x)), res))))


def cipher2(c, l, k):
    res = []
    tmp = False
    for i in range(l):
        res.append(tmp ^ c[i])
        tmp ^= res[-1]
        if i >= k-1:
            tmp ^= res[-(k)]

    print("".join(list(map(lambda x: str(int(x)), res))))


if __name__ == "__main__":
    arg = [int(x) for x in input().split()]
    _c = [int(x) for x in input()]
    cipher2(list(map(bool, _c)), arg[0], arg[1])
