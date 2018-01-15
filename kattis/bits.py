def solve(x):
    result = 0

    for i in range(len(x)):
        result = max(result, "{0:b}".format(int(x[:i+1])).count('1'))

    print(result)


for _ in range(int(input())):
    solve(input())
