n, m = map(int, input().split())
c = list(sorted(map(int, input().split())))
print(min(min(c[:n])*n*3, min(c[n:2*n])/2*n*3, m))
