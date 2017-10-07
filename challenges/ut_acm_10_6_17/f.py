count = dict()

for _ in range(int(input())):
    token = ''.join(input().split())

    count[token] = count.get(token, 0) + 1

for token in ['RR', 'GG', 'BB']:
    if token in count:
        count.pop(token)

result = 0

for u in ['RG', 'RB', 'GB']:
    v = ''.join(reversed(u))

    swaps = min(count.get(u, 0), count.get(v, 0))

    count[u] = count.get(u, 0) - swaps
    count[v] = count.get(v, 0) - swaps

    result += swaps

result += sum(count.values()) * 2 // 3

print(result)
