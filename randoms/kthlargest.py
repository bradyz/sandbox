def kth(a, k):
    def pivot(s, e):
        val = a[s]
        left = s
        right = e
        while left < right:
            while a[left] <= val:
                left += 1
            while a[right] > val:
                right -= 1
            if left < right:
                a[left], a[right] = a[right], a[left]
        a[s] = a[right]
        a[right] = val
        return right
    l = len(a)
    pivot(0, l-1)
    print(a)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        el = int(input())
        arr = [int(val) for val in raw_input().split()]
        print(kth(arr, el))
