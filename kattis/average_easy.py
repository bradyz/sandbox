def solve(cs, econ):
    cs_avg = sum(cs) / len(cs)
    econ_avg = sum(econ) / len(econ)

    result = 0

    for x in cs:
        if x < cs_avg and x > econ_avg:
            result += 1

    print(result)


for _ in range(int(input())):
    input()
    input()

    cs = list(map(int, input().split()))
    econ = list(map(int, input().split()))

    solve(cs, econ)
