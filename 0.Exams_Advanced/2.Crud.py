import re

matrix = []
matrix_size = 6
for i in range(matrix_size):
    matrix.append(input().split())

starting_input = input()
rows, cols = "", ""
pattern = r"(?P<rows>\d{1}), (?P<cols>\d{1})"
for match in re.findall(pattern, starting_input):
    rows = int(match[0])
    cols = int(match[1])
start_position = [rows, cols]
# start_position = list(map(int, input().strip("(").strip(")").split(", ")))

while True:
    current_command = input().split(", ")
    command = current_command[0]
    if command == "Stop":
        break
    direction = current_command[1]

    position = []
    if direction == "up":
        position = [start_position[0] - 1, start_position[1]]
    elif direction == "down":
        position = [start_position[0] + 1, start_position[1]]
    elif direction == "left":
        position = [start_position[0], start_position[1] - 1]
    elif direction == "right":
        position = [start_position[0], start_position[1] + 1]

    row, col = position[0], position[1]

    if command == "Create":
        value = current_command[2]
        if matrix[row][col] == ".":
            matrix[row][col] = value
    elif command == "Update":
        value = current_command[2]
        if matrix[row][col] != ".":
            matrix[row][col] = value
    elif command == "Delete":
        if matrix[row][col] != ".":
            matrix[row][col] = "."
    elif command == "Read":
        if matrix[row][col] != ".":
            print(matrix[row][col])

    start_position = position

for row in matrix:
    print(*row)
