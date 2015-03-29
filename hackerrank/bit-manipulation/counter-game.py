def counter_game(c):
    i = 0
    while int(c) > 1:
        tmp = "1" + "0" * (len(c)-1)
        if c == tmp:
            c = tmp[:-1]
        else:
            c = bin(int(c, 2) - int(tmp, 2)).lstrip("0b")
        i += 1
    if i % 2 == 0:
        print("Richard")
    else:
        print("Louise")

if __name__ == "__main__":
    for _ in range(int(input())):
        _c = bin(int(input())).lstrip("0b")
        counter_game(_c)
