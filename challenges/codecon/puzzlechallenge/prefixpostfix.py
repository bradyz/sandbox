o = {"+", "-", "*", "/", "^"}
c = input().split()


def operate(a, b, c):
    a = int(a)
    b = int(b)
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a // b
    elif c == "^":
        return a ** b
    return False

cont = True

while cont and len(c) > 2:
    cont = False
    if c[2] in o and c[1] not in o and c[0] not in o:
        c[:3] = [operate(c[0], c[1], c[2])]
        cont = True
    if not cont:
        c = list(reversed(c))
        for i in range(2, len(c)):
            if c[i] in o and c[i-1] not in o and c[i-2] not in o:
                c[i-2:i+1] = [operate(c[i-1], c[i-2], c[i])]
                cont = True
                c = list(reversed(c))
                break

if len(c) != 1:
    print("invalid")
else:
    print(c[0])
