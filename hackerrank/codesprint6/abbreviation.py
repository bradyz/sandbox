def can(a, b):
    if not b:
        return all(not x.isupper() for x in a)
    elif not a and b:
        return False
    if a[0].isupper():
        if a[0] == b[0]:
            return can(a[1:], b[1:])
        return False
    if a[0] == b[0]: 
        return can(a[1:], b[1:]) or can(a[1:], b)
    elif a[0].upper() == b[0]:
        return can(a[1:], b[1:]) or can(a[1:], b)
    return can(a[1:], b)


for _ in range(int(input())):
    if can(input(), input()):
        print("YES")
    else:
        print("NO")
