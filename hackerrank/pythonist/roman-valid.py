r = "M CM D CD C XC L XL X IX V IV I"
v = r.split()
n = input()
i = 0
j = 0

while i < len(v) and j < len(v):
    t = len(v[i])
    if n[j:j+t] == v[i]:
        j += t
    else:
        i += 1

print(i, j)
if j == len(n):
    print("True")
else:
    print("False")
