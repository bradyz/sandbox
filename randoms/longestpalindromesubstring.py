word = "forgeekskeegfor"


def solve(c):
    r_b = -1
    r_e = -1

    for i in range(len(c)):
        for j in range(min(i+1, len(c)-i)):
            if c[i+j] != c[i-j]:
                break
            if 2 * j > (r_e - r_b):
                r_b = i-j
                r_e = i+j
        for j in range(min(i+1, len(c)-i-1)):
            if c[i+j+1] != c[i-j]:
                break
            if (2 * j + 1) > (r_e - r_b):
                r_b = i-j
                r_e = i+j+1

    return c[r_b:r_e+1]

print(solve(word))
