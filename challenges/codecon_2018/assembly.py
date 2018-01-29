def _int(x):
    try:
        return int(x)
    except:
        return 0

lines = [input().split() for _ in range(int(input()))]

index = 0
values = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g':0, 'h':0}

while True:
    instruction = lines[index]

    if instruction[0] == 'set':
        _, a, b = instruction
        b = values.get(b) or _int(b)

        values[a] = b
    elif instruction[0] == 'add':
        _, a, b = instruction
        b = values.get(b) or _int(b)

        values[a] += b
    elif instruction[0] == 'sub':
        _, a, b = instruction
        b = values.get(b) or _int(b)

        values[a] -= b
    elif instruction[0] == 'mul':
        _, a, b = instruction
        b = values.get(b) or _int(b)

        values[a] *= b
    elif instruction[0] == 'mod':
        _, a, b = instruction
        b = values.get(b) or _int(b)

        values[a] %= b
    elif instruction[0] == 'div':
        _, a, b = instruction
        b = values.get(b) or _int(b)

        values[a] //= b
    elif instruction[0] == 'jmp':
        _, a = instruction
        a = values.get(a) or _int(a)

        index += a or 1
        continue
    elif instruction[0] == 'ret':
        print(values[instruction[1]])
        break
    else:
        print(instruction)

    index += 1
