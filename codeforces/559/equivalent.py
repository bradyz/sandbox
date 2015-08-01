def f(s):
    if len(s) % 2:
        return s
    a = f(s[:len(s) // 2])
    b = f(s[len(s) // 2:])
    if a < b:
        return a+b
    else:
        return b+a

if f(input()) == f(input()):
    print("YES")
else:
    print("NO")
