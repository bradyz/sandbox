from itertools import combinations


def prob_win(knight, opp):
    return 0

num_test = int(input())

for test in range(num_test):
    num_knights = int(input())
    prob = [int(x) for x in raw_input().split()]
    me = prob[0]
    prob = prob[1:]
    win = prob_win(me, prob)
