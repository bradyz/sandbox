from collections import Counter


def sansa_xor(c, s):
    count = Counter()
    res = 0
    for i in range(s):
        count[c[i]] += ((s-i-1)*(i+1)) + (i+1)
    for i in count:
        if count[i] % 2 == 1:
            res ^= i
    print(res)
    return 0

for _ in range(int(input())):
    _s = int(input())
    _c = list(map(int, input().split()))
    sansa_xor(_c, _s)
