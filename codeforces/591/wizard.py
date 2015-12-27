l = int(input())
p = int(input())
q = int(input())
t = l / (p + q)
pos_p = l - p * t
print(l - pos_p)
