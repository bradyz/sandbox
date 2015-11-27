def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

if __name__ == "__main__":
    A, B, C, D = map(int, input().split())
    total = 0
    for a in range(1, A+1):
        for b in range(1, B+1):
            for c in range(1, C+1):
                for d in range(1, D+1):
                    r = True
                    r &= (a - b) % 3 == 0
                    r &= (b + c) % 5 == 0
                    r &= (a * c) % 4 == 0
                    r &= gcd(a, d) == 1
                    total += r
    print(total)
