n = int(input())
a = 0
b = 0
c = 0
d = 1
for i in range(n):
    pa, pb, pc, pd = a, b, c, d
    a = pb + pc + pd
    b = pa + pc + pd
    c = pa + pb + pd
    d = pa + pb + pc
print(d % 1000000007)
