matrix_size = int(input())
matrix = []
position = []
burrows = []

for r in range(matrix_size):
    current_row = list(input())
    matrix.append(current_row)
    if "S" in current_row:
        c = current_row.index("S")
        position = [r, c]
    if "B" in current_row:
        for t_index in range(len(current_row)):
            if current_row[t_index] == "B":
                burrows.append([r, t_index])

food_quantity = 0
out = False

while food_quantity < 10:
    command = input()
    next_position = []
    if command == "up":
        next_position = [position[0] - 1, position[1]]
    elif command == "down":
        next_position = [position[0] + 1, position[1]]
    elif command == "left":
        next_position = [position[0], position[1] - 1]
    elif command == "right":
        next_position = [position[0], position[1] + 1]

    matrix[position[0]][position[1]] = "."
    row, col = next_position[0], next_position[1]

    if row in range(len(matrix)) and col in range(len(matrix)):
        matrix[position[0]][position[1]] = "."
        if matrix[row][col] == "*":
            matrix[row][col] = "S"
            food_quantity += 1
        if matrix[row][col] == "B":
            matrix[row][col] = "."
            burrow_exit = burrows[1]
            next_position = [burrow_exit[0], burrow_exit[1]]
        position = next_position
    else:
        out = True
        break

if out:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")
for rows in matrix:
    print("".join(rows))
