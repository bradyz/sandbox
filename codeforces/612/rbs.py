BRACKETS = "{ }, [ ], < >, ( )"
openers = dict()
closers = dict()
for opener, closer in map(lambda x: x.split(), BRACKETS.split(",")):
    openers[opener] = closer
    closers[closer] = opener
stack = list()
impossible = False
res = 0
for char in input():
    if char in openers:
        stack.append(char)
    else:
        if not stack:
            impossible = True
            break
        elif stack[-1] != closers[char]:
            res += 1
        stack.pop()
impossible |= len(stack) > 0
if impossible:
    print("Impossible")
else:
    print(res)
