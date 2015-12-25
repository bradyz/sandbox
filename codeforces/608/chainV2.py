n = int(input())
pos_blast = [list(map(int, input().split())) for _ in range(n)]
MAX_N = max(pos_blast, key=lambda x: x[0])[0] + 2
power = [0 for _ in range(MAX_N)]
tower = [False for _ in range(MAX_N)]
can_destroy = [0 for _ in range(MAX_N)]
for pos, blast in pos_blast:
    pos += 1
    tower[pos] = True
    power[pos] = blast
for i in range(1, MAX_N):
    if not tower[i]:
        can_destroy[i] = can_destroy[i-1]
    else:
        can_destroy[i] = can_destroy[max(0, i - power[i] - 1)] + 1
print(n - max(can_destroy))
