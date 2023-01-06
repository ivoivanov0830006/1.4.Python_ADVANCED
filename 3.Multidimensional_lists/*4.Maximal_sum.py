import sys

rows, columns = [int(x) for x in input().split(' ')]
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]

max_sum = - sys.maxsize
max_sub_matrix = []
for r in range(len(matrix) - 2):
    for c in range(len(matrix[r]) - 2):
        sub_matrix_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + \
                         matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2] + \
                         matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]

        if sub_matrix_sum > max_sum:
            max_sum = sub_matrix_sum
            max_sub_matrix = [matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]], \
                             [matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]], \
                             [matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]]

print(f"Sum = {max_sum}")
for row in max_sub_matrix:
    print(*row, sep=" ")


"""
Write a program that reads a rectangular matrix's dimensions and finds the 3x3square with a maximum sum of its elements. There will be no case with two or more 3x3 squares with equal maximal sum.
Input
⦁	On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
⦁	On the following lines, you will receive each row with its columns - integers, separated by a single space in the range [-20, 20]
Output
⦁	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
⦁	On the following 3 lines, print each element of the found submatrix, separated by a single space
Examples
Input	Output
4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4	 	Sum = 75
1 4 14
7 11 2
8 12 16
5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5		Sum = 34
2 5 6 
5 4 1 
6 0 5

"""
