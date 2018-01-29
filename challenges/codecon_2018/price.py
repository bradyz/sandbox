m = int(input())
mult_ret = [list(map(float, input().split())) for _ in range(m)]
n = int(input())
pass_drive = [list(map(float, input().split())) for _ in range(n)]

result = list()

for p, d in pass_drive:
    if p <= d:
        result.append(1.0)
        continue

    for mult, ret in mult_ret:
        if 0.01 * ret * p > d:
            continue

        result.append(mult)
        break

print(' '.join(map(str, result)))
