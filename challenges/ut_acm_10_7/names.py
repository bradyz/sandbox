for _ in range(int(input())):
    names = set([str(input().split()[0]) for _ in range(5)])
    if len(names) == 5:
        print("HAPPINESS")
    else:
        print("DISAPPOINTMENT")
