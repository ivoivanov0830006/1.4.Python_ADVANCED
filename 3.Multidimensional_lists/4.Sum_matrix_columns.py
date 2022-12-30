rows, columns = (int(x) for x in input().split(", "))
total_sum = 0

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

columns_sums = [0] * columns
for row_index in range(rows):
    for column_index in range(columns):
        columns_sums[column_index] += matrix[row_index][column_index]

[print(x) for x in columns_sums]


"""
------------------------------------- Another Solution ---------------------------------

rows, columns = (int(x) for x in input().split(", "))
total_sum = 0

matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

columns_sums = [sum([row[i] for row in matrix]) for i in range(0, len(matrix[0]))]
for result in columns_sums:
    print(result)

------------------------------------ Problem to resolve --------------------------------

Write a program that reads a matrix from the console and prints the sum for each column on separate lines. 
On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will 
get elements for each column separated with a single space. 
-------------------------------------- Example inputs ----------------------------------
Input	
3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0	
Output
12
10
19
20
8
7	
Input	
3, 3
1 2 3
4 5 6
7 8 9	
Output
12
15
18

"""
