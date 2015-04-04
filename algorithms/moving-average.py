def brute_force(c, k):
    res = [v for v in c]
    for i in range(len(c)):
        for j in range(1, k+1):
            if i+j < len(c):
                res[i] += c[i+j]
            if i-j >= 0:
                res[i] += c[i-j]
    print(res)


def moving_av(c, k):
    avs = [0 for _ in range(len(c)+2*k)]

    avs[k] = sum(c[:k+1])

    print(avs)

    for i in range(1, len(c)):
        avs[i+k] = avs[i+k-1] + c[i] - avs[i-k]
        print(avs)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = moving_av(a, 1)
    c = brute_force(a, 1)
