cell = [["a", 1],
        ["a", 1],
        ["a", 1],
        ["b", 2],
        ["b", 2],
        ["c", 3],
        ["c", 3]]

counter = 0
num_cells = len(cell)
current = 0

for i in range(num_cells-1):
    # if the entry is the same, then merge
    if cell[current][0] == cell[current + 1][0]:
        cell[current][1] += cell[current + 1][1]
        cell.pop(current + 1)
    else:
        current += 1

print(cell)
