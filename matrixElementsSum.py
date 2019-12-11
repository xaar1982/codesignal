def matrixElementsSum(matrix):
    result = 0
    x = len(matrix)
    y = len(matrix[0])
    
    zeros = []
    for i in range(x):
        for j in range(y):
            if matrix[i][j] == 0:
                zeros.append([i,j])
    for zero in zeros:
        for i in range(zero[0] + 1,x):
            matrix[i][zero[1]] = 0
    for i in range(x):
        for j in range(y):
            result += matrix[i][j]
    return result
