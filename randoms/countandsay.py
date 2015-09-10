def countandsay(times=5, num="1"):
    print(num)

    if not times:
        return

    r = ""

    c = 1
    p = num[0]

    for v in num[1:]:
        if v != p:
            r += str(c) + p
            c = 0
        c += 1
        p = v

    r += str(c) + p

    countandsay(times-1, r)

if __name__ == "__main__":
    countandsay()
