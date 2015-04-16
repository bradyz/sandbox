def solution(c):
    c = sorted(c, key=lambda x: x[1])
    res = [c[0]]
    for i in range(1, len(c)):
        if c[i][0] >= res[-1][1]:
            res.append(c[i])
    print(res)


if __name__ == "__main__":
    a = [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9),
         (9, 11), (11, 14), (13, 16)]
    solution(a)
