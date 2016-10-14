c = [input().lower() for _ in range(int(input()))]
seen = dict()
r = 0
for word in c:
    count = dict()
    for char in word:
        count[char] = count.get(char, 0) + 1
    hashed = ""
    for char in sorted(count):
        hashed += char + str(count[char])
    seen[hashed] = seen.get(hashed, 0) + 1
print(sum(seen[x] for x in seen if seen[x] > 1))
