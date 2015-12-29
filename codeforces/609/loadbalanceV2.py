from math import ceil, floor

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    avg = s / n
    res = 0
    if avg % 1 == 0:
        avg = int(avg)
        for val in a:
            res += abs(avg - val)
    else:
        m = s % n
        new = [ceil(s/n) for _ in range(m)] + [floor(s/n) for _ in range(n-m)]
        a.sort()
        new.sort()
        for i in range(n):
            res += abs(a[i] - new[i])
    res = res // 2
    print(res)
