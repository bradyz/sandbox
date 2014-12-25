if __name__ == "__main__":
    lines = []
    with open('anagram-input.txt', 'r') as f:
        lines = f.readlines()

    a = lines[0]
    b = lines[1]

    print(a == b)
    print(sorted(a) == sorted(b))
