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
