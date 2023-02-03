matrix = []
matrix_size = int(input())
position = []
coals = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

input_directions = [x for x in input().split()]

for i in range(matrix_size):
    current_row = input().split()
    matrix.append(current_row)
    if "s" in current_row:
        position = [i, current_row.index("s")]
    if "e" in current_row:
        end_position = [i, current_row.index("e")]
    if "c" in current_row:
        for coal_index in range(len(current_row)):
            if current_row[coal_index] == "c":
                coals.append([i, coal_index])

game_over = False

for direction in input_directions:

    row, col = position[0] + directions[direction][0], position[1] + directions[direction][1]
    matrix[position[0]][position[1]] = "*"

    if 0 <= row < len(matrix) and 0 <= col < len(matrix):

        if matrix[row][col] == "*":
            matrix[row][col] = "s"
        elif matrix[row][col] == "c":
            matrix[row][col] = "s"
            coals.remove([row, col])
            if not coals:
                print(f"You collected all coal! ({row}, {col})")
                break
        elif matrix[row][col] == "e":
            print(f"Game over! ({row}, {col})")
            game_over = True
            break

        position = [row, col]

if coals and not game_over:
    print(f"{len(coals)} pieces of coal left. ({position[0]}, {position[1]})")
