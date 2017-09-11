draws = 0
ark = 0
knave = 0

for _ in range(int(input())):
    b, w = map(int, input().split())
    total = b + w

    if total % 4 == 0 and total % 2 == 0:
        draws += 1
    elif total % 4 != 0 and total % 2 != 0:
        draws += 1
    elif total % 2 == 0:
        ark += 1
    elif total % 4 == 0:
        knave += 1

print('Draws: %d' % draws)
print('Ark Won: %d' % ark)
print('Knave Won: %d' % knave)
