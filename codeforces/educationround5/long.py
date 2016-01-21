a = input().lstrip("0")
b = input().lstrip("0")
if len(a) > len(b):
    print(">")
elif len(a) < len(b):
    print("<")
else:
    equal = True
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        if a[i] > b[i]:
            print(">")
        elif a[i] < b[i]:
            print("<")
        equal = False
        break
    if equal:
        print("=")
