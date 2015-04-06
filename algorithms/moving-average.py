# O(n^2) adding up averages
def brute_force(c, k):
    res = [v for v in c]

    for i in range(len(c)):
        for j in range(1, k+1):
            if i+j < len(c):
                res[i] += c[i+j]
            if i-j >= 0:
                res[i] += c[i-j]

    print(res)


# O(k+n) adding up averages
def moving_av(c, k):
    avs = [0 for val in c]
    avs[0] = sum(c[:k+1])

    for i in range(1, len(c)):
        avs[i] = avs[i-1]
        if i+k < len(c):
            avs[i] += c[i+k]
        if i-(k+1) >= 0:
            avs[i] -= c[i-k-1]

    print(avs)


if __name__ == "__main__":
    a = [2, 4, 6, 8, 10, 12, 14, 16]
    print(a)
    b = moving_av(a, 2)
    c = brute_force(a, 2)
