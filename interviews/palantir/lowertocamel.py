instr = 'the quick brown fox'
# The Quick Brown Fox


def lowerToCap(myString):
    # ['the', 'quick', 'brown', 'fox']
    res = []
    dif = ord('A') - ord('a')
    for token in myString.split():
        tmp = [y for y in token]
        if ord(tmp[0]) >= ord('a'):
            tmp[0] = chr(ord(token[0]) + dif)
            res.append("".join(tmp))
    return " ".join(res)

print(lowerToCap(instr))
