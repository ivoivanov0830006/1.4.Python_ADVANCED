number_rows = int(input())

# matrix = [[int(x) for x in input().split(" ")] for _ in range(number_rows)]
matrix = []
for _ in range(number_rows):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)


primary_diagonal = []
secondary_diagonal = []
for row_index in range(len(matrix)):
    for column_index in range(len(matrix)):
        if row_index == column_index:
            primary_diagonal.append(matrix[row_index][column_index])
        if row_index == len(matrix) - column_index - 1:
            secondary_diagonal.append(matrix[row_index][column_index])

diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(diff)


"""
------------------------------------ Problem to resolve --------------------------------

Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold
the values for each column - N numbers separated by a single space. Print the absolute difference between 
the primary and the secondary diagonal sums.
-------------------------------------- Example inputs ----------------------------------
Input
3
11 2 4
4 5 6
10 8 -12	
Output
15	
Comments
Primary diagonal: sum = 11 + 5 + (-12) = 4
Secondary diagonal: sum = 4 + 5 + 10 = 19
Difference: |4 - 19| = 15
-------------------------------------------------
Input
4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14	
Output
34	

"""
