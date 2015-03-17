def largest_perm(arr, k):
    e = len(arr)
    for i in range(len(arr)):
        if arr[i] != e - i:
            idx = arr.index(e-i)
            arr[i], arr[idx] = e-i, arr[i]
            k -= 1
            if k == 0:
                break
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    nk = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    largest_perm(nums, nk[1])
