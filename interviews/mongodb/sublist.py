from collections import Counter


def is_sublist(l1, l2):
    is_sub = True
    print(l1)
    print(l2)
    l1_count = Counter()
    l2_count = Counter()

    for x in l1:
        l1_count[x] += 1

    for y in l2:
        l2_count[y] += 1

    for x in l1_count.keys():
        if x in l2_count.keys() and l1_count[x] <= l2_count[x]:
            continue
        else:
            is_sub = False
            break

    return is_sub

if __name__ == "__main__":
    with open('sublist-input.txt', 'r') as f:
        lines = f.readlines()

    a = []
    b = []
    for i, line in enumerate(lines):
        if i % 2 == 0:
            a = [int(i) for i in line.split()]
        else:
            b = [int(i) for i in line.split()]
            is_sub = is_sublist(a, b)
            print("A: " + str(a) + " B: " + str(b) + "\nis_sub: " + str(is_sub))
