s = input()
t = input()
n = int(input())
k = -1

for i in range(min(len(s), len(t))):
    if s[i] != t[i]:
        break
    k = i

n -= len(s) + len(t) - 2 * (k + 1)

while n > 0:
    if k == -1:
        n = 0
    else:
        k -= 1
        n -= 2

if n == 0:
    print("Yes")
else:
    print("No")
