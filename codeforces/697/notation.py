a, b = input().split(".")
c, d = b.split("e")
d = int(d)
if d >= 0:
    c = c + (d - len(c)) * "0"
    r = a + c[:d] + "." + c[d:]
else:
    if -d >= len(a):
        r = "0." + (-d - len(a)) * "0" + a[d:] + c
    else:
        r = a[:-d] + "." + a[-d:] + c
if r[-2:] == ".0":
    print(r[:-2])
else:
    print(r.rstrip("."))
