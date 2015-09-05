def solve(w):
    c = 0

    for i in range(len(w) // 2):
        if w[i] != w[len(w) - 1 - i]:
            if c > 0:
                return "NO"
            c += 1
        i += 1

    return "YES"

for _ in range(int(input())):
    print(solve(input()))
