def merge(l1,l2):
    l = []
    global count
    while l1 and l2:
        if l1[-1] < l2[-1]:
            l.append(l2.pop())
            count += len(l1)
        else:
            l.append(l1.pop())
    l.reverse()
    return l1 + l2 + l

def sort(l):
    t = len(l) // 2
    return merge(sort(l[:t]), sort(l[t:])) if t > 0 else l


n = int(input())
arr = [0] + list(map(int, input().split()))

count = 0

for i in range(1, n+1):
    arr[i] += arr[i-1]

sort(arr)

print(count)
