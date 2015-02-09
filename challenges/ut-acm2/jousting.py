from itertools import combinations


def prob_win(opp):
    if len(opp) == 2:
        return opp[0] / (opp[0] + opp[1])
    it = iter(opp)
    for x in it:
        pa = x
        pb = next(it)


num_test = int(input())

for test in range(num_test):
    num_knights = int(input())
    prob = [int(x) for x in raw_input().split()]
    win = prob_win(prob)
