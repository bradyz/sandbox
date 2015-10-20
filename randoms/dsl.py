import operator


class DSL:
    def __init__(self, program):
        self.stack = list()
        self.labels = dict()
        self.program = program
        self.index = 0

    def parse(self):
        while self.index < len(self.program):
            FUNC = {"push": self.push, "print": self.pprint, "goto": self.goto}
            OPERATORS = {"add": operator.add, "sub": operator.sub,
                         "mult": operator.mul, "div": operator.floordiv}

            command = self.program[self.index]

            # push 5 => ["push", "5"]
            parsed = command.split()
            action = parsed[0]
            args = parsed[1:]

            print(command)

            # valid command
            if action == "push":
                self.push(args[0])
            elif action == "label":
                self.create_label(args[0])
            elif action in OPERATORS:
                self.manipulate(OPERATORS[action])
            else:
                FUNC[action]()

    def goto(self):
        spot = self.stack.pop()
        if spot.isdigit():
            self.index = spot
        else:
            self.index = self.labels[spot]

    def create_label(self, name):
        self.labels[name] = self.index
        self.index += 1

    def push(self, val):
        self.stack.append(val)
        self.index += 1

    def pprint(self):
        assert(len(self.stack) > 0)
        print(self.stack.pop())
        self.index += 1

    def manipulate(self, operation):
        assert(len(self.stack) >= 2)
        self.stack.append(operation(int(self.stack.pop()),
                                    int(self.stack.pop())))
        self.index += 1

if __name__ == "__main__":
    program = ["label start", "push 1", "push 2", "add", "print",
               "push start", "goto"]
    d = DSL(program)
    d.parse()
