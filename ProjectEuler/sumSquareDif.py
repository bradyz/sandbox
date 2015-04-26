a = 0
b = 0

for i in range(1, 101, 1):
    a += i * i

for i in range(1, 101, 1):
    b += i

b *= b

c = b - a
print(c)
