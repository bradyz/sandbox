import sys

counts = dict()

for line in sys.stdin:
    tmp = line.strip()

    counts[tmp] = counts.get(tmp, 0) + 1

max_count = 0
max_result = None

for key, val in counts.items():
    if val > max_count:
        max_count = val
        max_result = key

print(max_result)
print(max_count)
