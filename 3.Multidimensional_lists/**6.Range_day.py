matrix_size = 5
matrix = []
position = []
targets_left = []
targets_down = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(matrix_size):
    current_row = input().split()
    matrix.append(current_row)
    if "A" in current_row:
        position = [i, current_row.index("A")]
    if "x" in current_row:
        for target_index in range(len(current_row)):
            if current_row[target_index] == "x":
                targets_left.append([i, target_index])

number_commands = int(input())

for _ in range(number_commands):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == "move":
        steps = int(command[2])
        row = position[0] + directions[direction][0] * steps
        col = position[1] + directions[direction][1] * steps

        if 0 <= row < len(matrix) and 0 <= col < len(matrix):
            if matrix[row][col] == ".":
                matrix[position[0]][position[1]] = "."
                matrix[row][col] = "A"
                position = [row, col]
            elif matrix[row][col] == "x":
                position = [position[0], position[1]]
        else:
            position = [position[0], position[1]]

    elif action == "shoot":
        row, col = position[0] + directions[direction][0], position[1] + directions[direction][1]
        while 0 <= row < len(matrix) and 0 <= col < len(matrix):
            if matrix[row][col] == "x":
                matrix[row][col] = "."
                targets_left.remove([row, col])
                targets_down.append([row, col])
                break
            row, col = row + directions[direction][0], col + directions[direction][1]
        if not targets_left:
            break
if not targets_left:
    print(f"Training completed! All {len(targets_down)} targets hit.")
else:
    print(f"Training not completed! {len(targets_left)} targets left.")
print(*targets_down, sep="\n")
