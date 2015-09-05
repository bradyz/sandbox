for _ in range(int(input())):
    c = 0
    for i, val in enumerate(map(int, input().split())):
        c += val != i+1
    if c <= 1:
        print("YES")
    else:
        print("NO")
