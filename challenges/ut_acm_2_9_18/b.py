n = int(input())
score = dict()
for _ in range(n):
    tmp = input().split()
    name = tmp[0]
    hap = float(tmp[1])

    score[name] = hap

result = 1

for _ in range(int(input())):
    result *= score[input()]

print(int(result))
