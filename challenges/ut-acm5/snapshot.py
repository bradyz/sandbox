from collections import Counter

for _ in range(int(input())):
    args = [int(v) for v in input().split()]
    pros = {}

    for p in range(args[0]):
        num = int(input())
        pros[p] = input().split()

    for e in range(args[2]):
        msgs = [int(v) for v in input().split()]
        all_sent = []

        for i, val in enumerate(msgs):
            for a in pros[i][:val]:
                all_sent.append(a[1])

        count = Counter(all_sent)

        no = False

        for c in count:
            if count[c] == 1:
                no = True
                break

        if not no:
            print("YES")
        else:
            print("NO")
