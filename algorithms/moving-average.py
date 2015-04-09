from copy import copy


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
    for i in range(1, len(c)):
        c[i] += c[i-1]

    d = copy(c)

    for i in range(len(d)):
        if i-k-1 < 0:
            start = 0
        else:
            start = c[i-k-1]
        if i+k >= len(d):
            end = d[-1]
        else:
            end = c[i+k]
        d[i] = end - start

    print(d)

if __name__ == "__main__":
    a = [2, 4, 6, 8, 10, 12, 14, 16]
    print(a)
    y = brute_force(a, 2)
    x = moving_av(a, 2)
