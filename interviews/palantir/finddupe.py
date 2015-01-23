import sys


def differs_by(arr, dist, val):
    for x in range(0, len(arr) - dist):
        for y in range(1, dist + 1):
            if abs(arr[x] - arr[x + y]) <= val:
                return "YES"
    return "NO"

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            num_cases = int(line.strip("\n"))
        elif i % 3 == 1:
            args = [int(x) for x in line.split()]
            dist_val = args[0]
            val_val = args[1]
        elif i % 3 == 2:
            a_list = [int(x) for x in line.split()]
        else:
            correct = line.strip("\n")
            result = differs_by(a_list, dist_val, val_val)
            print("Correct: " + correct + " Result: " + result)
