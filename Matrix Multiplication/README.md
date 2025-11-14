# 🚀 Matrix Multiplication Program (Normal + Complex Numbers)

A simple yet powerful Python-based Matrix Multiplication Tool that supports:

✔ Normal Matrix
✔ Complex Number Matrix
✔ Normal × Complex combinations

This program allows users to input the matrix size, enter values (including complex numbers like 3+4j, 2-7j), and generates the final product matrix.

## ✨ Features

🔢 Supports any size matrices

🧮 Handles normal and complex numbers

❎ Built-in validation for dimension mismatch

⚡ Fast and clean multiplication logic

🎯 Beginner-friendly, easy to understand

💻 Pure Python, no external libraries

❤️ Created with love by Saad Shaikh

## 📌 How It Works

Enter rows & columns for Matrix 1

Enter its elements (normal or complex)

Enter rows & columns for Matrix 2

Enter its elements

The program validates dimensions

Final multiplied matrix is displayed

## 🧠 Supported Inputs

You can enter values in formats like:

5
7.3
3+4j
2-6j
8j


Python automatically converts them into complex numbers.

## 📂 Code Overview
Core Functions
🔹 input_matrix(num)

Takes matrix number (1 or 2), asks for dimensions and elements.

🔹 multiply_matrices(A, Arows, Acols, B, Brows, Bcols)

Performs matrix multiplication with complex support.

🔹 display_matrix(matrix)

Prints the final result in matrix form.

## 🧩 Example Run
--- Enter Matrix 1 ---
Enter number of rows: 2
Enter number of columns: 2
Enter elements (normal or complex). Example: 5 or 3+4j or 2-6j
Enter element at (1, 1): 2
Enter element at (1, 2): 1+2j
Enter element at (2, 1): 3
Enter element at (2, 2): 4

--- Enter Matrix 2 ---
Enter number of rows: 2
Enter number of columns: 1
Enter element at (1, 1): 3
Enter element at (2, 1): 4+5j

--- Resultant Matrix ---
[(2*3 + (1+2j)*(4+5j))]


Output appears in Python list matrix form.

## 📜 Full Code
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
    if Acols != Brows:
        print("\nMatrix multiplication NOT possible!")
        print(f"Columns of Matrix 1 ({Acols}) != Rows of Matrix 2 ({Brows})")
        exit()

    result = [[0 for _ in range(Bcols)] for _ in range(Arows)]

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

## 🧪 Requirements

Python 3.x

No external libraries required

## ▶️ Run the Program
python matrix_multiply.py

## 📄 License

This project is open-source and free to use.

## ⭐ Support the Project

If you like this program, feel free to:

## 🌟 Star the repository

## 🤝 Contribute improvements

## 🗣 Share it with others

# 💙 Made with passion by Saad Shaikh
