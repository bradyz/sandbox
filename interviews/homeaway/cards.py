import random

suits = {'Heart', 'Diamond', 'Club', 'Spade'}
values = [int(x) for x in range(1, 14)]


class Deck:
    def __init__(self):
        self.pile = [None] * 52
        count = 0
        for s in suits:
            for v in values:
                tmp = Card(s, v)
                self.pile[count] = tmp
                count += 1

    def show_cards(self):
        for x in self.pile:
            print x.val, x.suit

    def shuffle(self):
        random.shuffle(self.pile)


class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

if __name__ == "__main__":
    print values
    a = Deck()
    a.shuffle()
    a.show_cards()
