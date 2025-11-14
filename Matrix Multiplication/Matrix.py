def input_matrix(num):
    print(f"\n--- Enter Matrix {num} ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter elements (normal or complex). Example: 5 or 3+4j or 2-6j")

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = complex(input(f"Enter element at ({i+1}, {j+1}): "))
            row.append(val)
        matrix.append(row)

    return matrix, rows, cols


def multiply_matrices(A, Arows, Acols, B, Brows, Bcols):
    # Condition for multiplication
    if Acols != Brows:
        print("\nMatrix multiplication NOT possible!")
        print(f"Columns of Matrix 1 ({Acols}) != Rows of Matrix 2 ({Brows})")
        exit()

    # Result matrix initialization
    result = [[0 for _ in range(Bcols)] for _ in range(Arows)]

    # Multiplying
    for i in range(Arows):
        for j in range(Bcols):
            for k in range(Acols):
                result[i][j] += A[i][k] * B[k][j]

    return result


def display_matrix(matrix):
    print("\n--- Resultant Matrix ---")
    for row in matrix:
        print(row)


# MAIN PROGRAM
A, Arows, Acols = input_matrix(1)
B, Brows, Bcols = input_matrix(2)

result = multiply_matrices(A, Arows, Acols, B, Brows, Bcols)

display_matrix(result)

print("------- Made with ❤️  by Saad Shaikh -------")
