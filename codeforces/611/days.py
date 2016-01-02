DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
line = input().split()
save = int(line[0])
res = 0
if line[2] == "week":
    num = 1
    while num <= 366:
        if (num + 3) % 7 == save - 1:
            res += 1
        num += 1
else:
    for days in DAYS:
        if save <= days:
            res += 1
print(res)
