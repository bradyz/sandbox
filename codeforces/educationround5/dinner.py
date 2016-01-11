n, m = map(int, input().split())
streets = [list(map(int, input().split())) for _ in range(n)]
print(max(map(lambda x: min(x), streets)))
