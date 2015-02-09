class Bst:
    def __init__(self):
        self.root = Node()


class Node():
    def __init__(self, value=None):
        self.p = None
        self.v = None
        self.l = None
        self.r = None

    def __str__(self):
        return "P: " + str(self.v) + " L: " + str(self.l) + " R: " + str(self.r)
