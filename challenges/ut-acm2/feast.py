from math import ceil

def min_price(m, p):
    cost = 0
    p = sorted(p, key=lambda costof: costof[3])
    while m[0] > 0 or m[1] > 0 or m[2] > 0:
        print(m)
        tmp_max = max(m)
        tmp_ind = m.index(tmp_max)
        p = sorted(p, key=lambda costof: costof[tmp_ind])
        num = ceil(m[tmp_ind] / p[len(p) - 1][tmp_ind])
        x = p[len(p) - 1]
        m[0] -= num * x[0]
        m[1] -= num * x[1]
        m[2] -= num * x[2]
        cost += num * x[3]
    print(m)
    return cost


num_test = int(input())

for test in range(num_test):
    args = raw_input()
    args = [int(x) for x in args.split()]
    farmers = args[0]
    meats = [args[1], args[2], args[3]]
    prices = []
    for farmer in range(farmers):
        farmprice = [int(x) for x in raw_input().split()]
        prices.append(farmprice)
    print(min_price(meats, prices))
