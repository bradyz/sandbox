for _ in range(int(input())):
    n = int(input())
    m = input()
    s = input()
    have = dict()
    need = dict()
    x = len(m) // n
    for i in range(n):
        tmp = m[i * x: i * x + x]
        have[tmp] = have.get(tmp, 0) + 1
    for i in range(n):
        tmp = s[i * x: i * x + x]
        need[tmp] = need.get(tmp, 0) + 1
    if have == need:
        print("YES")
    else:
        print("NO")
