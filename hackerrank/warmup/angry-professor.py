def angry_professor(c, n, k):
    count = 0
    for val in c:
        if val <= 0:
            count += 1
    if count < k:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    for _ in range(int(input())):
        args = [int(x) for x in input().split()]
        _n = args[0]
        _k = args[1]
        _c = [int(x) for x in input().split()]
        angry_professor(_c, _n, _k)
