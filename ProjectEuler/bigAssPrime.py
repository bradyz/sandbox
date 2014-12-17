import math

top = 110000
a = range(2, top+1)
b = math.floor(math.sqrt(top))
prime = 2
y = 1
count = 1

for x in a:
    prime = x
    y = a.index(prime) + 1
    while y < len(a):
        if(a[y] % prime == 0):
            a.pop(y)
        else:
            y += 1
    print "%d \t %d" % (count, prime)
    if(count == 100001):
        break
    count += 1
