from copy import copy
from itertools import product


class AxiomChecker:
    # _r => the list of all possible elements
    # _p => the solution of all plus operations
    @staticmethod
    def a2(_r, _p):
        for i in range(len(_r)):
            for j in range(len(_r)):
                for k in range(len(_r)):
                    a = _r[i]
                    b = _r[j]
                    c = _r[k]
                    ab = _p[frozenset([a, b])]      # (a+b)
                    bc = _p[frozenset([b, c])]      # (b+c)
                    ab_c = _p[frozenset([ab, c])]   # (a+b)+c
                    a_bc = _p[frozenset([a, bc])]   # a+(b+c)
                    if ab_c != a_bc:                # checking equality
                        return False
        return True

    # _r => the list of all possible elements
    # _t => the solution of all times operations
    # _p => the solution of all plus operations
    @staticmethod
    def md(_r, _t, _p):
        for i in range(len(_r)):
            for j in range(len(_r)):
                for k in range(len(_r)):
                    a = _r[i]
                    b = _r[j]
                    c = _r[k]
                    bpc = _p[frozenset([b, c])]     # (b+c)
                    axb = _t[frozenset([a, b])]     # (axb)
                    axc = _t[frozenset([a, c])]     # (axc)
                    if _t[frozenset([a, bpc])] != _p[frozenset([axb, axc])]:
                        return False
        return True


class RingGenerator:
    def __init__(self, n=3):
        self.n = n
        self.r = ["0", "1"] + [chr(ord("A")+i) for i in range(n-2)]
        self.comb = set()
        self.add = {}
        self.mult = {}
        self.seed_add()
        self.seed_mul()
        self.poss_add = []
        self.poss = []
        for i in range(self.n):
            for j in range(i, self.n):
                self.comb.add(frozenset([self.r[i], self.r[j]]))

    def add_rule(self, x, y, z):
        self.add[frozenset([x, y])] = z

    def mult_rule(self, x, y, z):
        self.mult[frozenset([x, y])] = z

    def get_mult(self, x, y):
        if frozenset([x, y]) in self.mult:
            return self.mult[frozenset([x, y])]
        else:
            return None

    def get_add(self, x, y):
        if frozenset([y, x]) in self.add:
            return self.add[frozenset([x, y])]
        else:
            return None

    def seed_add(self):
        for i in range(self.n):
            for j in range(i, self.n):
                if self.r[i] == "0":
                    self.add_rule(self.r[i], self.r[j], self.r[j])
                elif self.r[j] == "0":
                    self.add_rule(self.r[i], self.r[j], self.r[i])

    def seed_mul(self):
        for i in range(self.n):
            for j in range(i, self.n):
                if self.r[i] == "0" or self.r[j] == "0":
                    self.mult_rule(self.r[i], self.r[j], "0")
                elif self.r[i] == "1":
                    self.mult_rule(self.r[i], self.r[j], self.r[j])
                elif self.r[j] == "1":
                    self.mult_rule(self.r[i], self.r[j], self.r[i])

    def add_solution(self):
        miss_add = list(self.comb - self.add.keys())
        for com in product(self.r, repeat=len(miss_add)):
            tmp = copy(self.add)
            for i in range(len(miss_add)):
                tmp[miss_add[i]] = com[i]
            if AxiomChecker.a2(self.r, tmp):
                self.mult_solution(tmp)

    def mult_solution(self, add_sol):
        miss_mult = list(self.comb - self.mult.keys())
        for com in product(self.r, repeat=len(miss_mult)):
            tmp = copy(self.mult)
            for i in range(len(miss_mult)):
                tmp[miss_mult[i]] = com[i]
            if AxiomChecker.md(self.r, tmp, add_sol):
                self.poss.append([add_sol, tmp])
                break

    def solution(self):
        self.add_solution()
        for (i, j) in self.poss:
            self.add = i
            self.mult = j

    def __str__(self):
        if not self.poss:
            return "No Solutions"

        res = "Addition of " + str(self.n) + " Elements\n"
        res += " " + "-" * ((self.n + 1) * 4 - 1) + "\n"
        res += "| + | " + " | ".join(self.r) + " |\n"
        for i in self.r:
            res += "|" + "---|" * (self.n + 1) + "\n"
            res += "| " + i + " | "
            res += " | ".join([self.get_add(i, x) for x in self.r])
            res += " |\n"
        res += " " + "-" * ((len(self.r) + 1) * 4 - 1) + "\n\n"

        res += "Multiplication of " + str(self.n) + " Elements\n"
        res += " " + "-" * ((self.n + 1) * 4 - 1) + "\n"
        res += "| x | " + " | ".join(self.r) + " |\n"
        for i in self.r:
            res += "|" + "---|" * (self.n + 1) + "\n"
            res += "| " + i + " | "
            res += " | ".join([self.get_mult(i, x) for x in self.r])
            res += " |\n"
        res += " " + "-" * ((len(self.r) + 1) * 4 - 1) + "\n"

        return res


class BoolRingGenerator(RingGenerator):
    def __init__(self, n=2):
        super(BoolRingGenerator, self).__init__(n)

    def seed_add(self):
        super(BoolRingGenerator, self).seed_add()
        for i in range(self.n):
            for j in range(i, self.n):
                if self.r[i] == self.r[j]:
                    self.add_rule(self.r[i], self.r[j], "0")

    def seed_mul(self):
        super(BoolRingGenerator, self).seed_mul()
        for i in range(self.n):
            for j in range(i, self.n):
                if self.r[i] == self.r[j]:
                    self.mult_rule(self.r[i], self.r[j], self.r[i])

a = BoolRingGenerator(4)
a.solution()
print(a)
