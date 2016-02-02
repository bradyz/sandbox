import json
for _ in range(int(input())):
    j = json.loads(input())
    grades = list()
    for k, v in j.items():
        if k == "serial" or v > 9:
            continue
        grades.append(v)
    print(int(sum(grades) / len(grades)))
