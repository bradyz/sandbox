def boyermoore(n, h):
    right = {}

    for i in range(len(n)):
        right[n[i]] = i

    i = 0
    found = False

    print(h)

    while i < len(h) and not found:
        print(" " * i + h[i:i+len(n)])
        found = True
        for j in range(len(n)-1, -1, -1):
            if n[j] != h[i+j]:
                if h[i+j] in right:
                    i += max(1, j - right[h[i+j]])
                else:
                    i += len(n)
                found = False
                break

    if found:
        print(i, h[i:i+len(n)])

if __name__ == "__main__":
    needle = "needle"
    haystack = "findingahaystackneedleina"
    boyermoore(needle, haystack)

    # Output:
    # findingahaystackneedleina
    # findin
    #      ngahay
    #            stackn
    #                 needle
