def pow_mod(x, y, z=1000000007):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number


k = int(input())
print(5 * pow_mod(9, k-1) * (pow_mod(10, k) - 1) % 1000000007)
