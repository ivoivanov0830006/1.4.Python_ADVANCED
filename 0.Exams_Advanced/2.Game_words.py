initial_string = list(map(str, input()))

matrix_size = int(input())
matrix = []
position = []

for r in range(matrix_size):
    current_row = list(input())
    matrix.append(current_row)
    if "P" in current_row:
        c = current_row.index("P")
        position = [r, c]

number_commands = int(input())

for _ in range(number_commands):
    command = input()
    next_position = []
    if command == "up":
        if position[0] == 0:
            next_position = [0, position[1]]
            if initial_string:
                last_letter = initial_string.pop()
        else:
            next_position = [position[0] - 1, position[1]]
    elif command == "down":
        if position[0] == matrix_size - 1:
            next_position = [matrix_size - 1, position[1]]
            if initial_string:
                last_letter = initial_string.pop()
        else:
            next_position = [position[0] + 1, position[1]]
    elif command == "left":
        if position[1] == 0:
            next_position = [position[0], 0]
            if initial_string:
                last_letter = initial_string.pop()
        else:
            next_position = [position[0], position[1] - 1]
    elif command == "right":
        if position[1] == matrix_size - 1:
            next_position = [position[0], matrix_size - 1]
            if initial_string:
                last_letter = initial_string.pop()
        else:
            next_position = [position[0], position[1] + 1]

    row, col = next_position[0], next_position[1]
    matrix[position[0]][position[1]] = "-"

    if matrix[row][col].isalpha():
        initial_string.append(matrix[row][col])
        matrix[row][col] = "P"

    if matrix[row][col] == "-":
        matrix[row][col] = "P"

    matrix[row][col] = "P"
    position = next_position

print("".join(initial_string))
for rows in matrix:
    print("".join(rows))
