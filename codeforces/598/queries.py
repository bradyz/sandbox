word = list(input())
for _ in range(int(input())):
    l, r, k = map(int, input().split())
    k %= r - l + 1
    word[l-1:r] = word[r-k:r] + word[l-1:r-k]
print("".join(word))
