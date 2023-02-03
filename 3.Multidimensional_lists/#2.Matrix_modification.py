matrix = [[int(x) for x in input().split()] for i in range(int(input()))]

while True:
    current_command = input()
    if current_command == "END":
        break
    command = current_command.split()
    action = command[0]
    row, col = int(command[1]), int(command[2])
    value = int(command[3])
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        current_value = matrix[row][col]
        if action == "Add":
            current_value += value
        if action == "Subtract":
            current_value -= value
        matrix[row][col] = current_value
    else:
        print("Invalid coordinates")

for r in matrix:
    print(*r)
