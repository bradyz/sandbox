import sys
sys.setrecursionlimit(10000)

def solve(c, d, s):
    if c == '':
        return ' '.join(s)

    for x in d:
        y = c[:len(x)]

        if x in y:
            s.append(x)

            tmp = solve(c[len(x):], d, s)

            if tmp:
                return tmp

            s.pop()

    return None


for _ in range(int(input())):
    input()
    d = set(input().split())
    c = input()

    print(solve(c, d, list()) or 'WRONG PASSWORD')
