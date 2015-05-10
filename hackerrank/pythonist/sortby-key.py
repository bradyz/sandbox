i, k = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(i)]
n = int(input())
g.sort(key=lambda x: x[n])
for x in g:
    print(" ".join(map(str, x)))
