import sys

if __name__ == "__main__":
    pi = "31415926535897932384626433833"

    for i, line in enumerate(sys.stdin):
        if i > 0:
            sent = line.split()
            idx = 0
            res = True
            while idx < len(sent) and res:
                if str(len(sent[idx])) != pi[idx]:
                    res = False
                idx += 1
            if res:
                print("It's a pi song.")
            else:
                print("It's not a pi song.")
