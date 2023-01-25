def get_children(m, r, c):
    possible_children_coordinates = [
        [r - 1, c - 1],
        [r - 1, c],
        [r - 1, c + 1],
        [r, c - 1],
        [r, c + 1],
        [r + 1, c - 1],
        [r + 1, c],
        [r + 1, c + 1]
    ]

    result = []
    for child_r, child_c in possible_children_coordinates:
        if 0 <= child_r < len(m) and 0 <= child_c < len(m):
            result.append([child_r, child_c])
    return result


matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    current_row = []
    for _ in range(matrix_size):
        current_row.append(0)
    matrix.append(current_row)

mines_count = int(input())
position = []

for _ in range(mines_count):
    command = list(map(int, input().strip("(").strip(")").split(", ")))
    row, col = command[0], command[1]
    matrix[row][col] = "*"

    children = get_children(matrix, row, col)
    for child in children:
        child_row, child_col = int(child[0]), int(child[1])
        if matrix[child_row][child_col] != "*":
            matrix[child_row][child_col] += 1

for row in matrix:
    print(*row)
