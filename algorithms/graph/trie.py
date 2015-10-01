def populate_tree():
    tree = dict()
    tree[""] = (dict(), False)

    for _ in range(int(input())):
        word = input()
        level = tree[""][0]

        for i, letter in enumerate(word):
            if letter not in level:
                level[letter] = (dict(), False)

            if i == len(word)-1:
                level[letter] = (level[letter][0], True)

            level = level[letter][0]

    return tree


def possible_words(prefix):
    def path(cur_level, pre):
        if cur_level[1]:
            result.append(pre)

        for letter in cur_level[0]:
            path(cur_level[0][letter], pre+letter)

    result = []
    level = tree[""][0]

    for letter in prefix:
        if letter not in level:
            return result

        level = level[letter][0]

    for letter in level:
        path(level[letter], prefix+letter)

    return result

if __name__ == "__main__":
    tree = populate_tree()

    print(possible_words("c"))
    print(possible_words("co"))
    print(possible_words(""))
