def fix_interval(x, y, n):
    if x >= n and y >= n:
        yield x % n, y % n
    elif y >= n:
        yield x, n-1
        yield 0, y % n
    else:
        yield x, y

n = int(input())
asked = list(map(int, input().split())) * 2
intervals = list()

for i in range(n, 2 * n):
    start = i - asked[i]
    if start >= i - n + 1:
        for x, y in fix_interval(i - n + 1, start, n):
            intervals.append((x, +1))
            intervals.append((y, -1))
intervals.sort(key=lambda x: (x[0], -x[1]))

result = 0
result_i = 0
current = 0
for x, y in intervals:
    current += y
    if current > result:
        result_i = x
        result = current
print(result_i + 1)
