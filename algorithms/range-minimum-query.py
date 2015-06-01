def process1(a, n):
    m = [[-1 for _ in range(n)] for _ in range(n)]
    m[0][0] = 0

    for i in range(n):
        for j in range(i+1, n):
            if a[m[i][j-1]] < a[j]:
                m[i][j] = m[i][j-1]
            else:
                m[i][j] = j

    return m

arr = [2, 4, 3, 1, 6, 7, 8, 9, 1, 7]
b = process1(arr, len(arr))

from pprint import PrettyPrinter
pp = PrettyPrinter()
pp.pprint(b)
