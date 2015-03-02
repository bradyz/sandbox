from random import randrange

def kth(a, k):
    def pivot(s, e):
        val = a[s]
        left = s
        right = e
        while left < right:
            while left < right and a[left] <= val:
                left += 1
            while a[right] > val:
                right -= 1
            if left < right:
                a[left], a[right] = a[right], a[left]
        a[s] = a[right]
        a[right] = val
        return right
    l = len(a)
    idx = 0
    while idx != l - k:
        tmp = pivot(idx, l-1)
        print("tmp: " + str(tmp) + " val: " + str(a[tmp]))
        if tmp > l - k + 1:
            idx -= 1
        else:
            idx += 1
        print(a)

    return a[-k:]

if __name__ == "__main__":
    arr = [randrange(100) for _ in range(10)]
    el = 2
    print(str(el) + " elements")
    print(arr)
    print(kth(arr, el))
    # t = int(input())
    # for _ in range(t):
    #     el = int(input())
    #     arr = [int(val) for val in raw_input().split()]
    #     print(el)
    #     print(arr)
    #     print(kth(arr, el))
