import re

actions = {('FB', 'F'): 'Homerun',
           ('C', 'S'): 'Hit',
           ('FB', 'S'): 'Strike',
           ('C', 'F'): 'Strike'}

plays = input()[1:-1]


strikes = 0
hits_in_a_row = 0
runs = 0
outs = 0

for line in re.findall(r'\((.*?)\)', plays):
    a, b = [x.strip() for x in line.split(',')]

    if actions[(a, b)] == 'Hit':
        strikes = 0

        hits_in_a_row += 1

        if hits_in_a_row == 4:
            runs += 1

            hits_in_a_row = 0
    elif actions[(a, b)] == 'Homerun':
        runs += (hits_in_a_row + 1)

        hits_in_a_row = 0
    elif actions[(a, b)] == 'Strike':
        strikes += 1

        if outs == 3:
            break
    else:
        print('fuck')

print(runs)
