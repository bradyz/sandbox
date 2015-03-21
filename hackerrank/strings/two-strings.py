def two_string(a, b):
    if len(set(a) & set(b)):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        first = input()
        second = input()
        two_string(first, second)
