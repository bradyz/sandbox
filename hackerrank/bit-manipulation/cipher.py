def cipher(c, l, k):
    res = int(c+"0"*k, 2)
    for i in range(1, k+1):
        res ^= int("0" * k + c + "0" * (k-i), 2)
    return 0

if __name__ == "__main__":
    arg = [int(x) for x in input().split()]
    _c = input()
    cipher(_c, arg[0], arg[1])
