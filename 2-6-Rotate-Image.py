from utils.timer import timer


@timer
def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n // 2 + n % 2):
            tmp = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] =  matrix[j][n-1-i]
            matrix[j][n-1-i] = matrix[i][j]
            matrix[i][j] = tmp
    return matrix


rotate([[1,2,3],[4,5,6],[7,8,9]])           # [[7,4,1],[8,5,2],[9,6,3]]
