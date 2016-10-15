import sys

input()

full_string = ""
cur = ""
time = 1

for i, line in enumerate(sys.stdin):
    if line.rstrip() == "END OF CASE":
        full_string = ""
        cur = ""
        time = 1
        continue

    cur += line[:-1]
    i = 0

    while i < len(cur):
        if cur[i] == ";":
            print(str(time) + ":", cur[:i+1])
            cur = cur[i+1:]
            i = 0
        i += 1

    time += 1
