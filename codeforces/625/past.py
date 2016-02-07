money = int(input())
plastic = int(input())
bottle = int(input())
change = int(input())
ret = 0
while money // plastic <= money // (bottle-change) and money // bottle > 0:
    liters = money // bottle
    money = money - liters * bottle + liters * change
    ret += liters
ret += money // plastic
print(ret)
