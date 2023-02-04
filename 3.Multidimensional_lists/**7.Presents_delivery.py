def cookie_func(current_directions, current_position):
    global presents_count
    for current_direction in current_directions.values():
        r, c = current_position[0] + current_direction[0], current_position[1] + current_direction[1]
        if matrix[r][c] == "X":
            presents_count -= 1
        if matrix[r][c] == "V":
            presents_count -= 1
            nice_kids_without_presents.remove([r, c])
            nice_kids_with_presents.append([r, c])
        matrix[r][c] = "-"
        if presents_count == 0:
            break
    return nice_kids_without_presents, nice_kids_with_presents


presents_count = int(input())
matrix_size = int(input())
matrix = []
position = []

nice_kids_without_presents = []
nice_kids_with_presents = []

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

for i in range(matrix_size):
    current_row = input().split()
    matrix.append(current_row)
    if "S" in current_row:
        position = [i, current_row.index("S")]
    if "V" in current_row:
        for target_index in range(len(current_row)):
            if current_row[target_index] == "V":
                nice_kids_without_presents.append([i, target_index])

while True:
    direction = input()
    if direction == "Christmas morning":
        break
    row, col = position[0] + directions[direction][0], position[1] + directions[direction][1]
    matrix[position[0]][position[1]] = "-"

    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if matrix[row][col] == "V":
            presents_count -= 1
            matrix[row][col] = "S"
            nice_kids_without_presents.remove([row, col])
            nice_kids_with_presents.append([row, col])
        if matrix[row][col] == "-":
            matrix[row][col] = "S"
        if matrix[row][col] == "X":
            matrix[row][col] = "S"
        if matrix[row][col] == "C":
            matrix[row][col] = "S"
            position = [row, col]
            cookie_func(directions, position)
            row, col = position[0], position[1]
        position = [row, col]
        if presents_count == 0 or len(nice_kids_without_presents) == 0:
            break

if presents_count == 0 and len(nice_kids_without_presents) > 0:
    print("Santa ran out of presents!")
for rows in matrix:
    print(*rows)
if nice_kids_without_presents:
    print(f"No presents for {len(nice_kids_without_presents)} nice kid/s.")
else:
    print(f"Good job, Santa! {len(nice_kids_with_presents)} happy nice kid/s.")
