for _ in range(int(input())):
    people = list()
    spots = dict()
    for i in range(int(input())):
        data = input().split()
        if data[0] == "DELETE":
            while people and spots[people[-1]] == -1:
                people.pop()
            if not people:
                print("NONE")
            else:
                spots[people[-1]] = -1
                print(people.pop())
        else:
            spots[data[1]] = i
            people.append(data[1])
    print()
