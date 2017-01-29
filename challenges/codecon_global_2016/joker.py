POINTS = {"J": 11, "Q": 12, "K": 13, "A": 14}
CARDS = "Jh Js Kh Qs Qh Ac Ah Jd Jc Qd Qc Kd Ks Kc As Ad".split()


def score(faces, suits):
    result = 0
    for k, v in faces.items():
        result += (v * v * POINTS[k])
    return result * max(suits.values())


def points(hand):
    faces = dict()
    suits = dict()
    for card in hand:
        if card == "Joker":
            continue
        faces[card[0]] = faces.get(card[0], 0) + 1
        suits[card[1]] = suits.get(card[1], 0) + 1
    result = score(faces, suits)
    if "Joker" in hand:
        for card in CARDS:
            faces[card[0]] = faces.get(card[0], 0) + 1
            suits[card[1]] = suits.get(card[1], 0) + 1
            result = max(result, score(faces, suits))
            faces[card[0]] = faces.get(card[0], 0) - 1
            suits[card[1]] = suits.get(card[1], 0) - 1
    return result


n = int(input())
hands = [list() for _ in range(n)]
deck = input().split()
for i in range(5):
    for j in range(n):
        hands[j].append(deck[i * n + j])
values = [(i, points(hand)) for i, hand in enumerate(hands)]
values.sort(key=lambda x: (-x[1], x[0]))
if values[0][1] == values[1][1]:
    print("tie", values[0][1])
else:
    print(values[0][0]+1, values[0][1])
