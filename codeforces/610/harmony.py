n = int(input())


def solve(k):
    if k == 0:
        return ['+']
    r = solve(k - 1)
    return [a + a for a in r] + [a + ''.join({'+': '*', '*': '+'}[c] for c in a) for a in r]

print("\n".join(map(str, solve(n))))
