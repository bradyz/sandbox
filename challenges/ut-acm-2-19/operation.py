OPS = set(["+", "-", "/", "*", "%"])


for _ in range(int(input())):
    c = list(input().split())
    o = input().split()
    n = len(c)
    error = False
    for op in o:
        if error:
            break
        for i in range(n):
            if c[i] != op:
                continue
            oper = c[i]
            left, l = None, -1
            right, r = None, -1
            for j in range(i-1, -1, -1):
                if c[j] == ".":
                    continue
                elif c[j] in OPS:
                    break
                left = int(c[j])
                l = j
            for j in range(i+1, n):
                if c[j] == ".":
                    continue
                elif c[j] in OPS:
                    break
                right = int(c[j])
                r = j
            if not left or not right:
                continue
            if oper == "+":
                c[i] = left + right
            elif oper == "-":
                c[i] = left - right
            elif oper == "*":
                c[i] = left * right
            elif oper == "%":
                if right == 0:
                    error = True
                    break
                c[i] = left % right
            elif oper == "/":
                if left % right != 0:
                    error = True
                    break
                c[i] = left // right
            c[r] = "."
            c[l] = "."
    ret = list()
    for v in c:
        try:
            ret.append(int(v))
        except:
            pass
    if len(ret) > 1 or error:
        print("OPERATION ERROR")
    else:
        print(ret[0])
