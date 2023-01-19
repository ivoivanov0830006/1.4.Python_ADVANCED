matrix = []
matrix_size = 6
position = []

for i in range(matrix_size):
    row = input().split()
    matrix.append(row)
    if "E" in row:
        position = [i, row.index("E")]

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

directions = input().split(", ")
for direction in directions:
    if direction == "up":
        if position[0] == 0:
            position[0] = matrix_size - 1
        else:
            position[0] -= 1
    elif direction == "down":
        if position[0] == matrix_size - 1:
            position[0] = 0
        else:
            position[0] += 1
    elif direction == "left":
        if position[1] == 0:
            position[1] = matrix_size - 1
        else:
            position[1] -= 1
    elif direction == "right":
        if position[1] == matrix_size - 1:
            position[1] = 0
        else:
            position[1] += 1

    row, col = position[0], position[1]

    if matrix[row][col] == "W":
        print(f"Water deposit found at ({row}, {col})")
        water_deposit += 1
    elif matrix[row][col] == "M":
        print(f"Metal deposit found at ({row}, {col})")
        metal_deposit += 1
    elif matrix[row][col] == "C":
        print(f"Concrete deposit found at ({row}, {col})")
        concrete_deposit += 1
    elif matrix[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
