n, p, q = map(int, input().split())
word = input()
p_factor = -1
q_factor = -1
for i in range(n // p + 1):
    if (n - i * p) % q == 0:
        p_factor = i
        q_factor = (n - i * p) // q
if p_factor != -1 and q_factor != -1:
    print(p_factor + q_factor)
    idx = 0
    for i in range(p_factor):
        print(word[idx:idx+p])
        idx += p
    for i in range(q_factor):
        print(word[idx:idx+q])
        idx += q
else:
    print(-1)
