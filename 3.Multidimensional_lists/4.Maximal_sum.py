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
