_, m = map(int, input().split())
c = map(int, input().split())
print(sum(m - x for x in c))
