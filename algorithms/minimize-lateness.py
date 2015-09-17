def minimize_lateness(time_deadlines):
    max_lateness = -1
    current_time = 0
    schedule = dict()

    time_deadlines.sort(key=lambda x: x[1])

    for time, deadline in time_deadlines:
        current_time += time
        max_lateness = max(max_lateness, current_time - deadline)
        schedule[time] = (time, deadline)

    print(max_lateness, schedule)


if __name__ == "__main__":
    c = [list(map(int, input().split())) for _ in range(int(input()))]

    minimize_lateness(c)
