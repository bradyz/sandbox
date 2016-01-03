bells, boxes = map(int, input().split())
weights = list(map(int, input().split()))

heaviest = -1

while boxes > bells // 2 and bells > 0:
    heaviest = max(heaviest, weights[bells-1])
    boxes -= 1
    bells -= 1

i, j = 0, bells-1
while i <= j:
    if i == j:
        heaviest = max(heaviest, weights[i])
    else:
        heaviest = max(heaviest, weights[i] + weights[j])
    i += 1
    j -= 1

print(heaviest)
