n = int(input())
while n >= 5:
    n >>= 1
    n -= 2
print(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"][n-1])
