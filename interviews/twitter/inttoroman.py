conv = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50,
        "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}


def roman_to_int(r):
    global conv
    i = 0
    res = 0
    size = len(r)
    print "yes " + str(size)

    while i < size:
        y = None
        x = r[i]
        if i < (size - 1):
            print size
            y = r[i: i+1]

        if y and y in conv.keys():
            res += conv[y]
            i += 2
        else:
            res += conv[x]
            i += 1

    return res


if __name__ == "__main__":
    with open('inttoroman-input.txt', 'r') as f:
        lines = f.readlines()

    for l in lines:
        rom = l.strip("\n")
        roman_to_int(rom)
        # print str(roman_to_int(rom))
        print ""
