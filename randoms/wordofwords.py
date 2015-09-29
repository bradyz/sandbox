def can_form(rest):
    if not rest:
        return False
    elif rest in dictionary:
        return True

    return any(can_form(rest[i:]) for i in range(len(rest))
               if rest[:i] in dictionary)


dictionary = [input() for _ in range(int(input()))]

print(can_form("hellocat"))
print(can_form("hellcat"))
print(can_form("hellcate"))
