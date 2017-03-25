n, v, t = map(int, input().split())
t = min(t, n)
expected = [0 for _ in range(n+1)]

for i in range(n):
    p, c, f = map(int, input().split())
    f = f / 100.0

    expected[i+1] = max(0, v * c * (1.0 - f) - p * f)

result = 0

for i in range(1, len(expected)):
    expected[i] += expected[i-1]

for i in range(t, len(expected)):
    result = max(result, expected[i] - expected[i-t])

print("%.10f" % result)
