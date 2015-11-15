two = []
power = 0
while 2 ** power <= 10**9:
    two.append(2 ** power)
    power += 1
for _ in range(int(input())):
    n = int(input())
    value = n * (n + 1) // 2
    two_value = 0
    for val in two:
        if val > n:
            break
        two_value += val
    print(value-2*two_value)
