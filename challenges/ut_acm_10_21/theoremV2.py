def solve(equation, rhs):
    actual = equation[0]
    for i in range(1, len(equation)):
        actual -= equation[i]
    if actual == rhs:
        print("correct")
        return

    can = set([equation[0] - equation[1]])
    for rhs_term in equation[2:]:
        new_can = set()
        for lhs in can:
            new_can.add(lhs - rhs_term)
            new_can.add(lhs + rhs_term)
        can = new_can

    if rhs in new_can:
        print("fixable")
    else:
        print("unfixable")


for _ in range(int(input())):
    line = input()
    left, right = line.split("=")
    left = list(map(int, left.split(" - ")))
    right = int(right)
    solve(left, right)
