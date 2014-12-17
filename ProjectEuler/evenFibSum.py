import sys

last = 4000000
x = 1
result = 0
y = 0

while(x < last):
    tmp = x
    x += y
    y = tmp
    if(x % 2 == 0):
        result += x

print result
