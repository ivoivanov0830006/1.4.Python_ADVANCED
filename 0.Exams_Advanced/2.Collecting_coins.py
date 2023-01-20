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


"""
------------------------------------ Problem to resolve --------------------------------

On the first line, you will be given a number representing the size of the field with a square 
shape. On the following few lines, you will be given the field with: 
    * One player - randomly placed in it and marked with the symbol "P"
    * Numbers for coins placed at different positions of the field
    * Walls marked with "X"
After the field state, you will be given commands for the player's movement. 
    Commands can be: "up", "down", "left", "right". 
    If the command is invalid, you should ignore it. 
The player moves in the given direction with one step for each command and collects all the coins 
that come across. If he goes out of the field, he should continue to traverse the field from the 
opposite side in the same direction.
Note: He can go through the same path many times, but he can collect the coins only the first time.
There are only two possible outcomes of the game:
    * The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to
    the next-lowest number.
    * The player collects at least 100 coins and wins the game.
If the player won the game, print: 
    "You won! You've collected {total_coins} coins."
If the player loses the game, print: 
    "Game over! You've collected {total_coins} coins."
Collected coins have to be rounded down to the next-lowest number.
The player's path as coordinates in lists on separate lines: 
"Your path:
[{row_position1}, {column_position1}]
[{row_position2}, {column_position2}]
…
[{row_positionN}, {column_positionN}]"
Constrains
There will be no case in which less than 100 coins will be in the field
All given numbers will be valid integers in the range [0, 100]
