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


"""
------------------------------------ Problem to resolve --------------------------------

Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, 
separated by a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum 
in the format:
    "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
    Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".
-------------------------------------- Example inputs ----------------------------------
Input	
3
1, 2, 3
4, 5, 6
7, 8, 9	
Output
Primary diagonal: 1, 5, 9. Sum: 15
Secondary diagonal: 3, 5, 7. Sum: 15

"""
