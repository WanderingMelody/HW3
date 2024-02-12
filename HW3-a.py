def transpose(matrix):
    # Trans EQ
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matrix_multiply(A, b):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(b[0])):
            sum_ = sum(A[i][k] * b[k][j] for k in range(len(A[i])))
            row.append(sum_)
        result.append(row)
    return result

def is_symmetric(matrix):
    # Matrix Symmetry Check
    return all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))

def is_positive_definite(matrix):
    try:
        # Perform Cholesky decomposition
        n = len(matrix)
        L = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                sum_ = sum(L[i][k] * L[j][k] for k in range(j))
                if i == j:
                    L[i][j] = (matrix[i][i] - sum_) ** 0.5
                else:
                    L[i][j] = (1.0 / L[j][j] * (matrix[i][j] - sum_))
        return all(L[i][i] > 0 for i in range(n))
    except:
        return False

def forward_substitution(L, b):
    n = len(L)
    y = [0] * n
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
        y[i] /= L[i][i]
    return y

def backward_substitution(U, y):
    n = len(U)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x

def cholesky_solve(matrix, b):
    # Solve the system using Cholesky decomposition
    n = len(matrix)
    L = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            sum_ = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = (matrix[i][i] - sum_) ** 0.5
            else:
                L[i][j] = (1.0 / L[j][j] * (matrix[i][j] - sum_))
    Lt = transpose(L)
    y = forward_substitution(L, b)
    x = backward_substitution(Lt, y)
    return x

def doolittle_solve(matrix, b):
    # Perform Doolittle decomposition
    n = len(matrix)
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]

    for i in range(n):
        L[i][i] = 1

    for i in range(n):
        for j in range(i, n):
            sum_ = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = matrix[i][j] - sum_

        for j in range(i + 1, n):
            sum_ = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (matrix[j][i] - sum_) / U[i][i]

    # Solve Ly = b
    y = [0] * n
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]

    # Solve Ux = y
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x

def main():
    # Both Matrix and solve
    A = [[1, -1, 3, 2], [-1, 5, -5, -2], [3, -5, 19, 3], [2, -2, 3, 21]]
    b = [15, -35, 94, 1]

    if is_symmetric(A) and is_positive_definite(A):
        print("The first Matrix is symmetric and positive definite. Solving using Cholesky method:")
        x = cholesky_solve(A, b)
    else:
        print("The First Matrix is not symmetric and positive definite. Solving using Doolittle method:")
        x = doolittle_solve(A, b)

    print("Solution:", x)

    D = [[4, 2, 4, 0], [2, 2, 3, 2], [4, 3, 6, 3], [0, 2, 3, 9]]
    c = [20, 36, 60, 122]

    if is_symmetric(D) and is_positive_definite(D):
        print("The Second Matrix is symmetric and positive definite. Solving using Cholesky method:")
        x = cholesky_solve(D, c)
    else:
        print("The Second Matrix is not symmetric and positive definite. Solving using Doolittle method:")
        x = doolittle_solve(D, c)

    print("Solution:", x)

if __name__ == "__main__":
    main()