N = 10 ** 6 + 1

result = [0 for _ in range(N)]

for i in range(N):
	tmp = str(i)

	result[i] = result[i-1] + int(len(tmp) == len(set(tmp)))

for _ in range(int(input())):
	l, r = map(int, input().split())

	print(result[r] - result[l-1])
