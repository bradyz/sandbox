def sub_anagrams(a):
    count = 0
    for i in range(len(a)):
        for s in range(1, len(a)):
            for j in range(i+1, len(a)-s+1):
                if sorted(a[i:i+s]) == sorted(a[j:j+s]):
                    count += 1
    print(count)


if __name__ == "__main__":
    for _ in range(int(input())):
        sub_anagrams(list(input()))
