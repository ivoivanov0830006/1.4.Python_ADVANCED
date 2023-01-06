def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


input_rows, input_columns = [int(x) for x in input().split(' ')]
matrix = [input().split(' ') for _ in range(input_rows)]

while True:
    command = input()
    if command == "END":
        break
    command_parts = command.split()

    if len(command_parts) != 5 or command_parts[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command_parts[1:]]

    if is_outside(row1, col1, input_rows, input_columns) or is_outside(row2, col2, input_rows, input_columns):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=" ")

        
------------------------------------- Another Solution ---------------------------------
def valid(current_command):
    row1, col1, row2, col2 = [x for x in command[1:]]
    if row1.isdigit() and col1.isdigit() and row2.isdigit() and col2.isdigit():
        if int(row1) < rows and int(row2) < rows and int(col1) < columns and int(col2) < columns:
            return True
    return False


rows, columns = [int(x) for x in input().split(' ')]
matrix = [input().split(' ') for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break
    action = command[0]
    if action == "swap" and len(command) == 5 and valid(command):
        r1 = int(command[1])
        c1 = int(command[2])
        r2 = int(command[3])
        c2 = int(command[4])
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        for row in matrix:
            print(*row, sep=" ")
    else:
        print("Invalid input!")
