r = []
for _ in range(2*int(input())):
    line = input()
    if not line:
        continue
    for c in ("(", ")", "+", "-", "*"):
        line = line.replace(c, "")
    line = line.lstrip("0")
    if not line:
        r.append("0")
    else:
        r.append(line)
print("\n".join(r))
