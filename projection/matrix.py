def matrix_multiplication(a,b):
    coloumns_a = len(a[0])
    rows_a = len(a)
    coloumns_b = len(b[0])
    rows_b = len(b);

    result_matrix = [[j for j in range(coloumns_b)] for i in range(rows_a)]
    if coloumns_a == rows_b:
        for x in range(rows_a):
            for y in range(coloumns_b):
                sum = 0
                for k in range(coloumns_a):
                    sum += a[x][k] * b[k][y]
                result_matrix[x][y]=sum
            return result_matrix
        else:
            print("Error! The coloums of the first matrix must be equal with the rows of the second matrix")