from bisect import bisect_right


n = int(input())
x = list(sorted(map(int, input().split())))
for _ in range(int(input())):
    print(bisect_right(x, int(input())))
