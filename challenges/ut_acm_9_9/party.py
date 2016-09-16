for _ in range(int(input())):
    f, px, py = map(int, input().split())
    fs = [[px, py]] + [list(map(int, input().split())) for _ in range(f)]
    print(sorted(fs, key=lambda x: x[0])[(f + 1) // 2][0],
            sorted(fs, key=lambda x: x[1])[(f + 1) // 2][1])
