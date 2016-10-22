def dp(i, j, equation, memo):
    if (i, j) in memo:
        return memo[(i, j)]
    elif i == j:
        return set([equation[i]])
    result = set()
    for k in range(i, j):
        for left in dp(i, k, equation, memo):
            for right in dp(k+1, j, equation, memo):
                result.add(left - right)
    memo[(i, j)] = result
    return result


def solve(equation, rhs):
    result = dp(0, len(equation)-1, equation, dict())
    actual = equation[0]
    for i in range(1, len(equation)):
        actual -= equation[i]
    if actual == rhs:
        print("correct")
    elif rhs in result:
        print("fixable")
    else:
        print("unfixable")


for _ in range(int(input())):
    line = input()
    left, right = line.split("=")
    left = list(map(int, left.split(" - ")))
    right = int(right)
    solve(left, right)
