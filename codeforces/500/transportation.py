# 500A: New York Transportation
# Start Time: 11:44 p.m. 5-2-15
# End Time: 11:46 p.m. 5-2-15

a, b = map(int, input().split())
c = list(map(int, input().split()))

i = 0

while i + 1 < b:
    i += c[i]

if i == b-1:
    print("YES")
else:
    print("NO")
