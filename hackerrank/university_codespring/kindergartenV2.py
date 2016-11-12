def solve(t, n):
    r = 0
    for i in range(n):
        if i - asked[(t+i) % n] >= 0:
            r += 1
    return r

n = int(input())
asked = list(map(int, input().split()))

result = 0
result_i = 0

for t in range(n):
    tmp = solve(t, n)
    if tmp > result:
        result = tmp
        result_i = t

print(result_i + 1)
