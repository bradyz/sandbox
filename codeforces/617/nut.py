n = int(input())
a = list(map(int, input().split()))
adj_cell = list()

total_adj = 0

for i in range(n):
    if a[i] == 0:
        continue
    adj = 0
    for j in range(i-1, -1, -1):
        if a[j] == 1:
            break
        adj += 1
        if j == 0:
            adj = 0
    adj_cell.append(adj+1)

ret = int(1 in a)

for val in adj_cell:
    ret *= val

print(ret)
