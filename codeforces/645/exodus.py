from collections import deque


n, k = map(int, input().split())
s = [False] + [x == "0" for x in input()]
i = 0
j = 0
ret = int(1e9)
win = int(1e9)
que = deque()
while j < n + 1:
    if len(que) >= k + 1:
        if j - i < win:
            win = j - i
            tmp = list(que)
            for k in tmp:
                ret = min(ret, max(k - tmp[0], tmp[-1] - k))
        i += 1
        while i < j and que and que[0] < i:
            que.popleft()
    else:
        j += 1
        if j < n + 1 and s[j]:
            que.append(j)
print(ret)
