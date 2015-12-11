n = int(input())
c = list(map(int, input().split()))
lesseq = [(1, True) for _ in range(n)]
moreeq = [(1, True) for _ in range(n)]
for i in range(1, n):
    if c[i] < c[i-1] and moreeq[i-1][1]:
        continue
    elif c[i] < c[i-1] and not moreeq[i-1][1]:
        moreeq[i] = (moreeq[i-1][0]+1, True)
    elif c[i] == c[i-1]:
        moreeq[i] = (moreeq[i-1][0]+1, moreeq[i-1][1])
    elif c[i] > c[i-1]:
        moreeq[i] = (moreeq[i-1][0]+1, False)
for i in range(1, n):
    if c[i] > c[i-1] and lesseq[i-1][1]:
        continue
    elif c[i] > c[i-1] and not lesseq[i-1][1]:
        lesseq[i] = (lesseq[i-1][0]+1, True)
    elif c[i] == c[i-1]:
        lesseq[i] = (lesseq[i-1][0]+1, lesseq[i-1][1])
    elif c[i] < c[i-1]:
        lesseq[i] = (lesseq[i-1][0]+1, False)
print(" ".join(map(lambda x: str(x[0]), (x for x in lesseq))))
print(" ".join(map(lambda x: str(x[0]), (x for x in moreeq))))
