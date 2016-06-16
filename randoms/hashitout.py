def answer(digest):
    def recur(i, prev):
        if i >= len(digest):
            return prev
        for j in range(256):
            if dp[prev[-1]][j] == digest[i]:
                prev.append(j)
                if recur(i+1, prev):
                    return prev
                prev.pop()
        return False

    dp = [[((i * 129) ^ j) % 256 for i in range(256)] for j in range(256)]

    return recur(1, [0])

digest = [0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]
print(answer(digest))
