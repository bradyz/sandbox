n = int(input())
s = list(input())
k = int(input()) % 26
for i in range(n):
    if s[i].isalpha():
        a = ord(s[i])
        if a >= ord("a") and a <= ord("z"):
            a += k
            if a > ord("z"):
                a = a % ord("z") + ord("a") - 1
        else:
            a += k
            if a > ord("Z"):
                a = a % ord("Z") + ord("A") - 1
        s[i] = chr(a)
print("".join(s))
