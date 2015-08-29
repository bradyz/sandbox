def powerset(s):
    def helper(cur, c):
        r.append(c)

        for i in range(cur+1, len(s)):
            helper(i, c + [s[i]])

    r = [[]]

    for i in range(len(s)):
        helper(i, [s[i]])

    print("\n".join(map(str, r)))


def powersetV2(s):
    combinations = ["0000"] + ["0"*(len(s)-len(bin(i))+2) + bin(i).lstrip("0b")
                               for i in range(1, 2 ** len(s))]

    print("\n".join(map(lambda x: str([s[i] for i, j in enumerate(x)
                                       if int(j)]), combinations)))

if __name__ == "__main__":
    the_set = [1, 2, 3, 4]
    powersetV2(the_set)
