def brute_force(i, activities, can_have, required, venues):
    if i == len(activities):
        return 1
    result = 0
    activity = activities[i]
    for possible in can_have[activity]:
        if venues[possible] >= required[activity]:
            venues[possible] -= required[activity]
            result += brute_force(i+1, activities, can_have, required, venues)
            venues[possible] += required[activity]
    return result


n = int(input())
venues = dict()
for _ in range(n):
    name, amount = input().split()
    venues[name] = int(amount)
m = int(input())
required = dict()
can_have = dict()
for _ in range(m):
    data = input().split()[1:]
    activity = data[0]
    can_have[activity] = data[2:]
    required[activity] = int(data[1])
all_activities = list(required.keys())
print(brute_force(0, all_activities, can_have, required, venues))
