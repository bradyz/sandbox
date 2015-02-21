if __name__ == "__main__":
    num_tests = int(input())

    for test in range(num_tests):
        num_soldiers = int(input())

        soldiers = {}
        for soldier in range(num_soldiers):
            tmp = raw_input().split()
            if tmp[2] in soldiers:
                soldiers[tmp[2]].append((tmp[0], tmp[1]))
            else:
                soldiers[tmp[2]] = [(tmp[0], tmp[1])]
        print("Test Case #" + str(test + 1) + ":")
        for i in sorted(soldiers.keys()):
            x = soldiers[i]
            x = sorted(x, key=lambda tup: (tup[1], tup[0]))
            for y in x:
                print(y[0] + " " + y[1])
