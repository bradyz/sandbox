for _ in range(int(input())):
    a = input()
    if a.isdigit() and int(a[0]) in [7, 8, 9] and len(a) == 10:
        print("YES")
    else:
        print("NO")
