def binary_search(lo, hi):
    while lo < hi:
        mi = (lo + hi) // 2
        cost, _ = get_cost(mi)

        if cost < d:
            lo = mi + 1
        else:
            hi = mi

    return lo


def get_cost(n):
    cost = 0
    need = {name: 0 for name in items}

    for name in items:
        required, have, price = items[name]

        if have < n * required:
            need_to_buy = (n * required - have)
            cost += need_to_buy * price

            need[name] = need_to_buy

    return cost, need


r, g, d = map(int, input().split())

items = dict()

for _ in range(g):
    line = input().split()

    name = line[0]

    required = int(line[1])
    have = int(line[2])
    price = int(line[3])

    items[name] = (required, have, price)


num = binary_search(1, r)
cost, need = get_cost(num)

while cost > d:
    num -= 1
    cost, need = get_cost(num)

print(num)

for item in sorted(need.keys()):
    print(item, need[item])
