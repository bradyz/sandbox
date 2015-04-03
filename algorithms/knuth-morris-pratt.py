# Knuth-Morris-Pratt String Searching Algorithm
# n*r construction of DFA (deterministic finite-state automaton)
# O(n+m) string search
# Advantages:       Trivial after DFA is constructed
#                   Worst case O(n+m)
# Disadvantages:    DFA size is dependent on radix-size and pattern size
#                   Could be very large for large alphabets(unicode)


def kmp(pat, txt):
    def construct():
        # essentially the alphabet, all possible choices
        con = sorted(set(txt))
        d = {}

        # initialize dict
        for c in con:
            d[c] = {}
            for i in range(len(pat)):
                d[c][i] = 0

        # x is restart state
        x = 0
        d[pat[0]][0] = 1

        # construct dfa
        for i in range(1, len(pat)):
            for j in range(len(con)):
                d[con[j]][i] = d[con[j]][x]

            # a correct match moves onto the next state
            d[pat[i]][i] = i+1

            # update fail state
            x = d[pat[i]][x]

        return d

    dfa = construct()
    j = 0

    for i in range(len(txt)):
        # jump from state to state
        j = dfa[txt[i]][j]

        # reaches end state of dfa - a match
        if j == len(a):
            return i - len(pat) + 1

    return -1

if __name__ == "__main__":
    a = "ABABAC"
    b = "BCBAABACAABABACAA"
    c = kmp(a, b)
    print(c)
