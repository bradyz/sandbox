if __name__ == "__main__":
    num_people = int(input())
    start = int(input())
    end = int(input())
    alive = {}

    for year in range(start, end+1):
        alive[year] = 0

    for person in range(num_people):
        args = [int(val) for val in raw_input().split()]
        birth = args[0]
        death = args[1]
        for y in range(birth, death):
            alive[y] = alive[y] + 1

    max_alive = 0
    years = []

    for year in alive:
        if alive[year] == max_alive:
            years.append(year)
        elif alive[year] > max_alive:
            max_alive = alive[year]
            years = [year]

    print(max_alive)
    print(years)
