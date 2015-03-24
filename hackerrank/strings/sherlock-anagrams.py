from collections import Counter


def sub_anagrams(a):
    count = 0
    for i in range(len(a)):
        for s in range(1, len(a)):
            c_i = Counter(a[i:i+s])
            for j in range(i+1, len(a)-s+1):
                if c_i == Counter(a[j:j+s]):
                    count += 1
    print(count)


if __name__ == "__main__":
    for _ in range(int(input())):
        sub_anagrams(list(input()))
