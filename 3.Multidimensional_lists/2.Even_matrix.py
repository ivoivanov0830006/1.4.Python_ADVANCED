rows = int(input())

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    new_row = []
    for number in row:
        if number % 2 == 0:
            new_row.append(number)
    matrix.append(new_row)
print(matrix)


"""
------------------------------------ Problem to resolve --------------------------------

Write a program that receives a matrix of numbers and prints a new one only with the numbers that
are even. Use nested comprehension for that problem.
On the first line, you will receive the rows of the matrix. On the next rows, you will get elements
for each column separated with a comma and a space ", ".
-------------------------------------- Example inputs ----------------------------------
Input
2
1, 2, 3
4, 5, 6
Output
[[2], [4, 6]]
---------------------------------
Input
4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67
Output
[[10, 24], [34, 110], [4, 12], []]
"""
