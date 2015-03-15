import sys


def is_smith(n):
    pf = []
    tmp = n
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                pf.append(i)
                n /= i
                break
    pf = map(str, pf)
    p = 0
    for val in pf:
        for num in val:
            p += int(num)
    if p == sum([int(x) for x in str(tmp)]):
        return 1
    else:
        return 0

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        num = int(line)
        print(is_smith(num))
