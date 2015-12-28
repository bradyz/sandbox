n, k = map(int, input().split())
segment = list()

# add "events" for number of overlaps
for _ in range(n):
    a, b = map(int, input().split())
    segment.append([a, 1])
    segment.append([b, -1])
segment.sort(key=lambda x: (x[0], -x[1]))
result = list()
left = None

# line sweep
for i in range(len(segment)):
    if i != 0:
        segment[i][1] += segment[i-1][1]
    if left is None and segment[i][1] >= k:
        left = segment[i][0]
    elif left is not None and segment[i][1] == k-1:
        result.append((left, segment[i][0]))
        left = None

print(len(result))
print("\n".join(map(lambda x: " ".join(map(str, x)), result)))
