def pf(x):
    result = 0
    z = 2
    factors = list()
    while z * z <= x:
        while x % z == 0:
            factors.append(z)
            result += 1
            x //= z
        z += 1
    if x > 1:
        result += 1
    return result


for _ in range(int(input())):
    x = int(input())
    winner = max(pf(x)-1, 0)
    if winner % 2 == 0:
        print("Bob wins after move %d" % winner)
    else:
        print("Alice wins after move %d" % winner)
