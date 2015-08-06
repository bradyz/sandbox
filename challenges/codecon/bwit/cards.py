a = ["k", "q", "j", "10", "9", "8", "7", "6", "5", "4", "3", "2", "a"]
b = set(["s", "c"])
r = set(["h", "d"])
n = int(input())

count = 0
moves = 0
prev = None
i = 0

c = list(reversed([input() for _ in range(n)]))

while c and count < n:
    found = False
    if not prev:
        if c[-1][1] != "k":
            moves = 999999
        else:
            found = True
    else:
        if prev[0] in r and c[-1][0] in b:
            found = True
        elif prev[0] in b and c[-1][0] in r:
            found = True
        if c[-1][1] != a[i]:
            found = False
    cur = c.pop()
    if not found:
        c.insert(0, cur)
        count += 1
    else:
        i = (i+1) % len(a)
        count = 0
        prev = cur

    moves += 1

if not c:
    print(moves)
else:
    print("you lose")
