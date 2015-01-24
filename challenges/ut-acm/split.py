import sys
from collections import Counter
from collections import OrderedDict

count = 1


def split_money(money, people, chores):
    global count
    payout = Counter()
    for person in people:
        tmp = people[person]
        for x in tmp:
            payout[person] += money / len(chores) / chores[x]
    print("Case #" + str(count) + ":")
    for person in people:
        a = "{0:.2f}".format(payout[person])
        print(person + ": " + str(a))
    count += 1

if __name__ == "__main__":
    tasks = -1
    person = "asd"
    num_people = -1
    for i, line in enumerate(sys.stdin):
        if i == 0:
            num_cases = int(line.strip("\n"))
        elif i > 0:
            if num_people <= 0 and tasks <= 0:
                task_list = Counter()
                args = line.split()
                num_people = int(args[0])
                amount = float(args[1])
                person_tasks = OrderedDict()
            elif num_people >= 0:
                if tasks > 0:
                    task = line.strip("\n")
                    task_list[task] += 1
                    if person not in person_tasks.keys():
                        person_tasks[person] = [task]
                    else:
                        person_tasks[person].append(task)
                    tasks -= 1
                    if num_people <= 0 and tasks <= 0:
                        split_money(amount, person_tasks, task_list)
                else:
                    args = line.split()
                    person = args[0]
                    tasks = float(args[1])
                    num_people -= 1
