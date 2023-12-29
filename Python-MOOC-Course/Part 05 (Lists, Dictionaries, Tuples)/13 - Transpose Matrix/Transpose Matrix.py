"""
Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.
Matrix:
1 2 3
4 5 6
7 8 9

Transposed Matrix:
1 4 7
2 5 8
3 6 9
"""
def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

if __name__ == "__main__":
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    transpose(matrix)   
    print(matrix) 