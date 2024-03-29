rows, columns = (int(x) for x in input().split(", "))
total_sum = 0

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    total_sum += sum(row)

print(total_sum)
print(matrix)


"""
------------------------------------ Problem to resolve --------------------------------

Write a program that reads a matrix from the console and prints:
⦁	The sum of all numbers in the matrix
⦁	The matrix itself
On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
On the next rows, you will get elements for each column separated by a comma and a space ", ".
-------------------------------------- Example inputs ----------------------------------
Input
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
Output
76
[[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
"""

