import sys

rows, columns = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

max_sum = - sys.maxsize
max_sub_matrix = []
for r in range(len(matrix) - 1):
    for c in range(len(matrix[r]) - 1):
        sub_matrix_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]

        if sub_matrix_sum > max_sum:
            max_sum = sub_matrix_sum
            max_sub_matrix = [matrix[r][c], matrix[r][c + 1]], [matrix[r + 1][c], matrix[r + 1][c + 1]]

for row in max_sub_matrix:
    print(*row, sep=" ")
print(max_sum)
