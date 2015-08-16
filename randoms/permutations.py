from functools import reduce

string = "ABC"


def permutations(word, used):
    if reduce(lambda x, y: x & y, used, True):
        yield ""
    for i in range(len(word)):
        if not used[i]:
            used_copy = type(used)(used)
            used_copy[i] = True
            for val in permutations(word, used_copy):
                yield word[i] + val


for val in permutations(string, [False for v in string]):
    print(val)
