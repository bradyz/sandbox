def cipher(c, l, k):
    res = [c[0]]
    for i in range(1, l):
        tmp = c[i]
        for j in range(min(k-1, len(res))):
            tmp ^= res[-(j+1)]
        res.append(tmp)

    print("".join(list(map(lambda x: str(int(x)), res))))

if __name__ == "__main__":
    arg = [int(x) for x in input().split()]
    _c = [int(x) for x in input()]
    cipher(list(map(bool, _c)), arg[0], arg[1])
