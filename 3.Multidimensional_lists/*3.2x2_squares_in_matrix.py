rows, columns = [int(x) for x in input().split(' ')]
matrix = [input().split(' ') for _ in range(rows)]

count = 0
sub_matrix = []
for r in range(len(matrix) - 1):
    for c in range(len(matrix[r]) - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            sub_matrix = matrix[r][c], matrix[r][c + 1], matrix[r + 1][c], matrix[r + 1][c + 1]
            count += 1

print(count)
