def bday(b, w, x, y, z):
    if x > y + z:
        print(b * (y+z) + w * y)
    elif y > x + z:
        print(b * x + w * (x+z))
    else:
        print(b * x + w * y)

if __name__ == "__main__":
    for _ in range(int(input())):
        bw = list(map(int, input().split()))
        xyz = list(map(int, input().split()))
        bday(bw[0], bw[1], xyz[0], xyz[1], xyz[2])
