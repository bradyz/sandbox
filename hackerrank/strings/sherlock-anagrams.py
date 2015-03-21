def sub_anagrams(a):
    print(a)


if __name__ == "__main__":
    n = [input() for _ in range(int(input()))]
    "\n".join(list(map(sub_anagrams, n)))
