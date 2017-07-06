def get_choose(n):
    choose = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n+1):
        choose[i][0] = 1
        choose[i][i] = 1

        for j in range(1, i):
            choose[i][j] = choose[i-1][j-1] + choose[i-1][j]

    return choose


choose = get_choose(10)

print('\n'.join(map(str, choose)))
