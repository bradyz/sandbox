import sys


def has_key(key_list, lock):
    closest = 999
    ind = -1

    print(key_list, lock)

    if(len(key_list) == 0):
        return "NO"

    for x in range(len(key_list)):
        tmp = int(key_list[x], 2) ^ int(lock, 2)
        tmp = bin(tmp).lstrip("0b").count("1")
        if tmp < closest:
            closest = tmp
            ind = x
            if tmp == 0:
                return "YES"

    lock = bin(int(key_list[ind], 2) ^ int(lock, 2)).lstrip("0b")
    key_list.pop(ind)

    return has_key(key_list, lock)

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            num_cases = int(line.strip("\n"))
        elif i > 0:
            if i % 3 == 2:
                lock = line.strip("\n")
            elif i % 3 == 0:
                key_list = line.split()
                print(has_key(key_list, lock))
