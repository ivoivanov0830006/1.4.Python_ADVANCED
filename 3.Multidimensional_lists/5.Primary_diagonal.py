def get_primary_diagonal(current_matrix):
    return sum(current_matrix[i][i] for i in range(len(current_matrix)))
    # len(matrix) because rows = columns


n = int(input())

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

print(get_primary_diagonal(matrix))
