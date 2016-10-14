for _ in range(int(input())):
    m, n = map(int, input().split())
    mat = [[0 for _ in range(n+1)] for _ in range(m+1)]
    I = list(map(int, input().split()))
    A = list(map(int, input().split()))
    J = list(map(int, input().split()))
    nonzero = 0
    x = 0
    for i in range(m+1):
        if i != 0:
            for _ in range(I[i] - I[i-1]):
                mat[i][J[x]] = A[x]
                x += 1
        else:
            for _ in range(I[i]):
                mat[i][J[x]] = A[x]
                x += 1
    for row in mat[1:]:
        print(" ".join(map(str, row[:-1])))
