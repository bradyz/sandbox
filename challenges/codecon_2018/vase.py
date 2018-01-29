import itertools


def destroy_row(x, zeroes, xs):
    for i in range(x+1, grid_size):
        if (x, i) in zeroes:
            break

        xs.add((x, i))

    for i in range(x-1, -1, -1):
        if (x, i) in zeroes:
            break

        xs.add((x, i))


def disable_col(x, zeroes, xs):
    for i in range(grid_size):
        if (i, x) in xs:
            continue

        zeroes.add((i, x))


def simulate(order):
    zeroes = set()
    xs = set()

    for x in order:
        disable_col(x, zeroes, xs)
        destroy_row(x, zeroes, xs)

    return len(xs)


grid_size, num_switches = map(int, input().split())
switches = [int(input())-1 for _ in range(num_switches)]
result = float('inf')

for order in itertools.permutations(switches):
    result = min(result, simulate(order))

print(result)
