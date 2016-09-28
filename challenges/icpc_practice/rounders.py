for _ in range(int(input())):
    n = [0] + list(map(int, list(input())))
    i = len(n) - 1
    c = False
    for i in range(len(n)-1, 1, -1):
        if n[i] + c + 5 >= 10:
            c = True
        else:
            c = False
    r = (int("".join(map(str, n[:2]))) + c) * 10 ** (len(n) - 2)
    print(r)
