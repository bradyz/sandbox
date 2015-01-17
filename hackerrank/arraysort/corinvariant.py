import sys

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while j >= 0 and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
            l[j+1] = key

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            size = int(line.strip("\n"))
        else:
            parsed = [int(x) for x in line.split()]
            insertion_sort(parsed)
            arr = " ".join(map(str, parsed))
            print(arr)
