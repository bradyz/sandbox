for _ in range(int(input())):
    priority = set([input() for _ in range(int(input()))])
    items = [input() for _ in range(int(input()))]
    yes = list()
    no = list()
    for item in items:
        if item in priority:
            yes.append(item)
        else:
            no.append(item)
    for a in list(sorted(yes)) + list(sorted(no)):
        print(a)
