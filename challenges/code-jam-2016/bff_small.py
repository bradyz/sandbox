from itertools import permutations


for t in range(1, int(input()) + 1):
    n = int(input())
    c = list(map(int, input().split()))
    r = 0
    for v in permutations(c):
        for i in range(1, n+1):
            a = 5
    print(t)
