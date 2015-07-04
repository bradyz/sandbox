import sys
print("".join(list(str(sum([int(line.strip()) for line in sys.stdin]))))[:10])
