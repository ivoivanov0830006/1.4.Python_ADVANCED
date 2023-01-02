number_rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(number_rows)]

primary_diagonal = []
secondary_diagonal = []
for row_index in range(len(matrix)):
    for column_index in range(len(matrix)):
        if row_index == column_index:
            primary_diagonal.append(matrix[row_index][column_index])
        if row_index == len(matrix) - column_index - 1:
            secondary_diagonal.append(matrix[row_index][column_index])

primary_diagonal_numbers = (", ".join(map(str, primary_diagonal)))
secondary_diagonal_numbers = (", ".join(map(str, secondary_diagonal)))

print(f'Primary diagonal: {primary_diagonal_numbers}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {secondary_diagonal_numbers}. Sum: {sum(secondary_diagonal)}')
