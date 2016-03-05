for _ in range(int(input())):
    a, b = map(int, input().split())
    candies = [list(map(int, input().split())) for _ in range(a)]
    ret = list()
    for _ in range(b):
        name, happiness, w, x, y, z = input().split()
        happiness, w, x, y, z = int(happiness), int(w), int(x), int(y), int(z)
        found = False
        for w1, x1, y1, z1 in candies:
            if w1 * w + x1 * x + y1 * y + z1 * z >= happiness:
                found = True
        if found:
            ret.append(name)
    ret.sort()
    print(" ".join(map(str, ret)))
