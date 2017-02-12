def help(value):
    ones = 0
    for c in bin(value).lstrip("0b"):
        ones += (c == "1")
    return ones % 2 != 0

for _ in range(int(input())):
    n = int(input())
    result = 0
    for x in map(int, input().split()):
        result += help(x)
    print(result)
