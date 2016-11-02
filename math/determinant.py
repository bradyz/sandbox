def determinant(A):
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    n = len(A)
    result = 0
    for i in range(n):
        submatrix = list()
        for x in range(1, n):
            submatrix.append([A[x][y] for y in range(n) if y != i])
        result += ((-1) ** i) * A[0][i] * determinant(submatrix)
    return result

if __name__ == "__main__":
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    det = determinant(A)
    print(det)
