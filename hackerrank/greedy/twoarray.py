def twoarray(a, b, k):
    a.sort()
    b.sort(reverse=True)
    for vals in zip(a, b):
        if sum(vals) < k:
            return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arg = [int(val) for val in raw_input().split()]
        match = arg[1]
        a_arr = [int(val) for val in raw_input().split()]
        b_arr = [int(val) for val in raw_input().split()]
        print(twoarray(a_arr, b_arr, match))
