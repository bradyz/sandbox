def solve(sell_price, materials, need_materials, selling):
    cost = 0
    for mat, num in need_materials.items():
        mult, price = materials[mat]
        if num % mult == 0:
            cost += price * num // mult
        else:
            cost += price * (num // mult + 1)
    made = 0
    for item, num in selling:
        made += sell_price[item] * num
    print(made - cost)


for _ in range(int(input())):
    n, m, o = map(int, input().split())
    sell_price = dict()
    needs = dict()
    for _ in range(n):
        item, sell = input().split()
        needs[item] = set(input().split())
        sell_price[item] = int(sell)
    materials = dict()
    for _ in range(m):
        item, num, price = input().split()
        num, price = int(num), int(price)
        materials[item] = (num, price)
    need_materials = dict()
    selling = list()
    for _ in range(o):
        item, num = input().split()
        selling.append((item, int(num)))
        for item in needs[item]:
            need_materials[item] = need_materials.get(item, 0) + int(num)
    solve(sell_price, materials, need_materials, selling)
