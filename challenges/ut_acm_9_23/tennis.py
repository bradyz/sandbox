val = {0: "love", 1: "15", 2: "30", 3: "40"}


for _ in range(int(input())):
    r, x, y = input().split()
    r = int(r)
    x = str(x)
    y = str(y)
    xc = 0
    yc = 0
    for _ in range(r-1):
        w = str(input())
        xc += (w == x)
        yc += (w == y)

        xz = val.get(xc, None)
        yz = val.get(yc, None)

        if xc <= 2 and xc == yc:
            print(xz, "all")
        elif (xz == "40" and yz == "40") or not xz or not yz:
            if xc == yc:
                print("deuce")
            elif xc > yc:
                print("advantage " + x)
            else:
                print("advantage " + y)
        else:
            print(xz, yz)
    input()
    if xc > yc:
        print(x, "won!")
    else:
        print(y, "won!")
