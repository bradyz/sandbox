for _ in range(int(input())):
    n, k = map(int, input().split())
    emails = [input() for _ in range(n)]
    ret = 0
    i, j = 0, 0
    while i < n and j < n:
        while i < n and emails[i] == "IMPORTANT":
            i += 1
        if i >= n:
            break
        j = i
        while j < i + k and j < n and emails[j] != "IMPORTANT":
            j += 1
        ret += min(1, j-i+1)
        i = j
    print(ret)
