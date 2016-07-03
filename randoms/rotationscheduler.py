jobs = int(input())
job_names = [input() for _ in range(jobs)]
num_people = int(input())
vacations = [list() for _ in range(num_people)]
dates = [list() for _ in range(num_people)]
for i in range(num_people):
    name, num_vacations = input().split()
    num_vacations = int(num_vacations)
    for _ in range(num_vacations):
        start, end = input().split("-")
        dates.append((start, end))
        month = int(start[0]) - 1
        vacations[i].append(month)
print(job_names)
print(vacations)
