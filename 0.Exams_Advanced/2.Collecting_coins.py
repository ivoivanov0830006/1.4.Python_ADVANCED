from math import floor

matrix_size = int(input())

matrix = []
position = []
path = []

for i in range(matrix_size):
    current_row = input().split()
    matrix.append(current_row)
    if "P" in current_row:
        position = [i, current_row.index("P")]
        path.append([i, current_row.index("P")])

total_coins = 0
win = False

while True:
    command = input()
    if command == "up":
        if position[0] == 0:
            position[0] = matrix_size - 1
        else:
            position[0] -= 1
    elif command == "down":
        if position[0] == matrix_size - 1:
            position[0] = 0
        else:
            position[0] += 1
    elif command == "left":
        if position[1] == 0:
            position[1] = matrix_size - 1
        else:
            position[1] -= 1
    elif command == "right":
        if position[1] == matrix_size - 1:
            position[1] = 0
        else:
            position[1] += 1
    else:
        continue

    row, col = position[0], position[1]
    if matrix[row][col] == "X":
        path.append([row, col])
        total_coins = floor(total_coins / 2)
        break
    elif matrix[row][col] == "P":
        path.append([row, col])
        continue
    else:
        path.append([row, col])
        total_coins += int(matrix[row][col])
        matrix[row][col] = "P"
        if total_coins >= 100:
            win = True
            break

if win:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")
print("Your path:")
for step in path:
    print(step)
