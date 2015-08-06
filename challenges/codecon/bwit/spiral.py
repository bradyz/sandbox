n = int(input())
c = [[0 for j in range(n)] for i in range(n)]
i = 0
j = 0
x = 2
move = 0
c[i][j] = 1

while x < n**2+1:
    if move == 0 and j+1 < n and c[i][j+1] == 0:
        c[i][j+1] = x
        j += 1
    elif move == 1 and i+1 < n and c[i+1][j] == 0:
        c[i+1][j] = x
        i += 1
    elif move == 2 and j-1 >= 0 and c[i][j-1] == 0:
        c[i][j-1] = x
        j -= 1
    elif move == 3 and i-1 >= 0 and c[i-1][j] == 0:
        c[i-1][j] = x
        i -= 1
    else:
        move = (1 + move) % 4
        continue
    x += 1

for v in c:
    print(" ".join(map(str, v)))
