input_size = list(map(int, input().split()))
matrix_rows, matrix_cols = input_size[0], input_size[1]

matrix = []
start_position = []

for r_index in range(matrix_rows):
    row = input().split()
    matrix.append(row)
    # PLAYER POSITION
    if "B" in row:
        start_position = [r_index, row.index("B")]

touched_enemies = 0
total_moves = 0

while True:
    command = input()
    if command == "Finish":
        break

    next_position = []
    if command == "up":
        next_position = [start_position[0] - 1, start_position[1]]
    elif command == "down":
        next_position = [start_position[0] + 1, start_position[1]]
    elif command == "left":
        next_position = [start_position[0], start_position[1] - 1]
    elif command == "right":
        next_position = [start_position[0], start_position[1] + 1]

    row, col = next_position[0], next_position[1]

    if matrix[row][col] == "O":
        next_position = start_position[0], start_position[1]

    elif matrix[row][col] == "P":
        matrix[row][col] = "-"
        touched_enemies += 1
        total_moves += 1
        next_position = [row, col]
        if touched_enemies == 3:
            break
    elif matrix[row][col] == "-":
        total_moves += 1
        matrix[start_position[0]][start_position[1]] = "-"
    else:
        next_position = start_position[0], start_position[1]

    start_position = next_position

print(f"Game over!\nTouched opponents: {touched_enemies} Moves made: {total_moves}")
