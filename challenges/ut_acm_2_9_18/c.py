SUB = ['-', ' ', 'E', 'O', 'I', 'A']
SUB = ['_', '3', '0', '1', '4']


max_sub = -1
max_res = None

for _ in range(int(input())):
    string = input()

    count = 0

    for c in string:
        if c in SUB:
            count += 1

    if count > max_sub:
        max_sub = count
        max_res = string

print(max_res, max_sub)
