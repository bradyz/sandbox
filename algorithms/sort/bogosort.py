# bogosort is a sorting algorithm where the list is shuffled
# until the entire list is sorted
# O(n * n!)

from random import shuffle
from random import randrange


def bogosort(arr):
    toShuffle = True
    while toShuffle:
        prev = arr[0]
        for x in range(1, len(arr)):
            if arr[x] >= prev:
                toShuffle = False
                prev = arr[x]
                continue
            else:
                toShuffle = True
                shuffle(arr)
                break
    return arr


if __name__ == "__main__":
    arr = [randrange(10) for i in range(10)]

    print("Unsorted: " + str(arr))
    print("Sorted: " + str(bogosort(arr)))
