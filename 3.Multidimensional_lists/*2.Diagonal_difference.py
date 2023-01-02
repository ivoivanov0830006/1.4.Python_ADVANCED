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
