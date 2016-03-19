from itertools import product as comb

word = "abcdef"
n, q = map(int, input().split())
rep = dict()
for _ in range(q):
    k, v = input().split()
    rep[k] = v
ret = set()
for x in comb(word, repeat=n):
    tmp = "".join(x)
    while tmp[:2] in rep:
        tmp = rep[tmp[:2]] + tmp[2:]
    if tmp == "a":
        ret.add(x)
print(len(ret))
