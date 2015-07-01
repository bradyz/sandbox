c = [1, 2, 4, 0, 0, 0, 1]


def walk(a):
    i = 0
    j = a[0]
    while j >= 0 and i < len(a):
        if a[i] > j-1:
            j = a[i]
        else:
            j -= 1
        i += 1
    if i == len(a):
        print("YES")
    else:
        print("NO")

walk(c)
