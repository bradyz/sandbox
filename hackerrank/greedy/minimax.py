import sys


answer = 0


def check(x):
    ret = sys.maxint
    for i in range(n):
        ret = min(ret, abs(x-arr[i]))
    return ret


def limits(x):
    global answer
    if x < A or x > B:
        return
    if check(x) > check(answer):
        answer = x

if __name__ == "__main__":
    n = int(input())
    arr = [int(val) for val in raw_input().split()]
    pq = [int(val) for val in raw_input().split()]
    A = pq[0]
    B = pq[1]
    answer = A

    limits(A)
    limits(B)

    for i in range(n):
        for j in range(i+1, n):
            limits((arr[i]+arr[j])/2)
    print(answer)
