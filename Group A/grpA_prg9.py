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

def multiplication(mat1, mat2, n):
    ans = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        ans.append(temp)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] += mat1[i][k] * mat2[k][j]
    for r in ans:
        print(r)

def transpose(mat, n):
    ans = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        ans.append(temp)
    for i in range(n):
        for j in range(n):
            ans[i][j] = mat[j][i]   
    for r in ans:
        print(r)


n = int(input("Enter N for NxN matrix = "))
print()

mat1 = []
print("Enter values for matrix 1: ")
for i in range(n):
    temp = []
    for j in range(n):
        val = int(input())
        temp.append(val)
    mat1.append(temp)
for r in mat1:
    print(r)
print()

mat2 = []
print("Enter values for matrix 2: ")
for i in range(n):
    temp = []
    for j in range(n):
        val = int(input())
        temp.append(val)
    mat1.append(temp)
for r in mat2:
    print(r)
print()

print("CHOOSE FROM THE GIVEN OPTIONS:")

while(True):
    print()
    op = int(input("1. Addition of two matrices\n"
                   "2. Subtraction of two matrices\n"
                   "3. Multiplication of two matrices\n"
                   "4. Transpose of a matrix\n"
                   "PRESS 0 TO EXIT.\n"))
    if op == 0:
        break
    if op == 1:
        addition(mat1, mat2)
    if op == 1:
        subtraction(mat1, mat2)
    if op == 1:
        multiplication(mat1, mat2, n)
    if op == 1:
        transpose(mat1, n)
    else:
        print("Wrong input!")
print()