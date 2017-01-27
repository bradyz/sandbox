a, b, c = map(int, input().split())
m = int(input())
x = list()
y = list()
for _ in range(m):
    cost, mouse = input().split()
    cost = int(cost)
    if mouse == "USB":
        x.append(cost)
    else:
        y.append(cost)
x.sort(reverse=True)
y.sort(reverse=True)
total = 0
amount = 0
while (x and (a > 0 or c > 0)) or (y and (b > 0 or c > 0)):
    if a > 0 and x:
        a -= 1
        total += 1
        amount += x.pop()
    elif b > 0 and y:
        b -= 1
        total += 1
        amount += y.pop()
    elif c > 0:
        if x and y:
            if x[-1] < y[-1]:
                total += 1
                amount += x.pop()
            else:
                total += 1
                amount += y.pop()
        elif x:
            total += 1
            amount += x.pop()
        else:
            total += 1
            amount += y.pop()
        c -= 1
print(total, amount)
