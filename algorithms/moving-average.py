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
    for i in range(len(c)):
        avs[i+k] = c[i]

    avs[k] = sum(c[:k+1])

    print(avs)

    for i in range(k-1, len(c)):
        print(avs[i+k-1], avs[i+k+k])
        avs[i+k] = avs[i+k-1] + avs[i+k+k]

        if i - k - 1 >= 0:
            avs[i+k] -= avs[i] - avs[i-1]
            print(avs[i], avs[i-1])

        print(avs)


if __name__ == "__main__":
    a = [1, 1, 1, 1, 1, 1, 1, 1]
    b = moving_av(a, 2)
    c = brute_force(a, 2)
