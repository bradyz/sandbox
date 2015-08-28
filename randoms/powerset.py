def powerset(s):
    def helper(cur, c):
        r.append(c)

        for i in range(cur+1, len(s)):
            helper(i, c + [s[i]])

    r = [[]]

    for i in range(len(s)):
        helper(i, [s[i]])

    print("\n".join(map(str, r)))

if __name__ == "__main__":
    the_set = [1, 2, 3, 4]
    powerset(the_set)
