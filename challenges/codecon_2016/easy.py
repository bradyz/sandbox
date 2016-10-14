s = list(input())
n = int(input())
i = 0
while i < len(s):
    i_i = i
    j = min(i + n, len(s)) - 1
    while i_i < j:
        s[i_i], s[j] = s[j], s[i_i]
        i_i += 1
        j -= 1
    i += 2 * n
print("".join(s))
