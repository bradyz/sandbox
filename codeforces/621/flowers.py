n, p = map(int, input().split())
flowers = [list(map(int, input().split())) for _ in range(n)]
primes = [r // p - (l - 1) // p for l, r in flowers]

ret = 0

for i in range(n):
    j = (i + 1) % n
    total1 = flowers[i][1] - (flowers[i][0] - 1)
    total2 = flowers[j][1] - (flowers[j][0] - 1)
    probnot1 = (total1 - primes[i]) / total1
    probnot2 = (total2 - primes[j]) / total2
    ret += (1 - probnot1 * probnot2)

print(ret * 2000)
