def solve(str):
    s = []
    t = str.split("+")
    for i in range(len(t)):
        if t[i] == "+":
            continue
        s.append(t[i])
    for _ in range(len(t)-1):
        s.append("+")
    for i in range(len(s)):
        if "*" not in s[i]:
            continue
        t = s[i].split("*")
        x = []
        for j in range(len(t)):
            x.append(t[j])
        for _ in range(len(t)-1):
            x.append("*")
        s[i] = x
    return "".join(map(lambda x: "".join(x), s))

a = "2*4*3+9*3+5"
print(solve(a))
