interested = [input() for _ in range(int(input()))]
n, budget = map(int, input().split())

costs = list()

for _ in range(n):
    item = input()
    cost = int(input())

    for x in interested:
        if x == item.split()[-1]:
            costs.append(cost)

costs.sort()

result = 0

for x in costs:
    if budget >= x:
        budget -= x
        result += 1
    else:
        break

print(result)
