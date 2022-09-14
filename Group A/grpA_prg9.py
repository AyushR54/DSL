def addition(mat1, mat2):
    matrix = []
    for rows in range(2):
        row = []
        for cols in range(2):
            col = mat1[rows][cols] + mat2[rows][cols]
            row.append(col)
        matrix.append(row)
    for i in range(2):
        print(matrix[i])

def subtraction(mat1, mat2):
    matrix = []
    for rows in range(2):
        row = []
        for cols in range(2):
            col = mat1[rows][cols] - mat2[rows][cols]
            row.append(col)
        matrix.append(row)
    for i in range(2):
        print(matrix[i])



mat1 = [
    [1, 2],
    [3, 4]
]

mat2 = [
    [5, 6],
    [7, 8]
]

addition(mat1, mat2)