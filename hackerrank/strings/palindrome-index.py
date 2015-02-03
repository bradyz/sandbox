import sys


def to_remove(string):
    string = list(string)
    need_remove = False
    to_remove = -1

    for x in range(len(string) / 2):
        front = x
        end = len(string) - x - 1
        if not need_remove:
            if string[front] != string[end]:
                need_remove = True
        else:
            if string[front] == string[end]:




    return to_remove

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            parsed = line.strip("\n")
            index = to_remove(parsed)
            print(index)
