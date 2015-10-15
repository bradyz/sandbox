def can_form(rest):
    if not rest:
        return False
    elif rest in dictionary:
        return True

    return any(can_form(rest[i:]) for i in range(len(rest))
               if rest[:i] in dictionary)


def can_formV2(rest):
    if rest in dictionary:
        return True

    for i in range(len(rest)+1):
        if rest[:i] in dictionary:
            if can_formV2(rest[i:]):
                return True

    return False


dictionary = [input() for _ in range(int(input()))]

print(can_form("hellocat"))
print(can_form("hellcat"))
print(can_form("hellcate"))

print(can_formV2("hellocat"))
print(can_formV2("hellcat"))
print(can_formV2("hellcate"))
