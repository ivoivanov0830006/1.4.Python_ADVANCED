matrix_size = int(input())
matrix = []
position = []

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

failed = False
tea = 0
while tea < 10:
    direction = input()
    row, col = position[0] + directions[direction][0], position[1] + directions[direction][1]
    matrix[position[0]][position[1]] = "*"

    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if matrix[row][col] == "R":
            matrix[row][col] = "*"
            failed = True
            break
        if matrix[row][col] == ".":
            matrix[row][col] = "*"
        if matrix[row][col].isdigit():
            num = int(matrix[row][col])
            tea += num
            matrix[row][col] = "*"
        position = [row, col]
    else:
        failed = True
        break

if failed:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row)

    
"""
------------------------------------ Problem to resolve --------------------------------

You will be given an integer n for the size of the Wonderland territory with a square shape. 
On the following n lines, you will receive the rows of the territory:
⦁	Alice will be placed in a random position, marked with the letter "A". 
⦁	On the territory, there will be bags of tea, represented as numbers. If Alice steps on a 
number position, she collects the tea bags and increases the quantity with the corresponding number.
⦁	There will always be one rabbit hole on the territory marked with the letter "R".
⦁	All of the empty positions will be marked with ".".
After the field state, you will be given commands for Alice's movements. Move commands can be: 
        "up", "down", "left" or "right".
When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does 
not need to continue collecting. Otherwise, if she steps on the rabbit hole or goes out of the 
territory, she can't return, and the program ends. 
In the end, the path she walked had to be marked with '*'.
For more clarifications, see the examples below.
Input
⦁	On the first line, you will be given the integer n – the size of the square matrix
⦁	On the following n lines - matrix representing the field (each position separated by " ")
⦁	On each of the following lines, you will be given a move command
Output
⦁	On the first line: 
⦁	If Alice steps on the rabbit hole or she go out of the territory, print: 
"Alice didn't make it to the tea party."
⦁	If she collected at least 10 bags of tea, print: 
"She did it! She went to the party."
⦁	On the following lines, print the matrix.
Constraints
⦁	Alice will always either go outside the Wonderland or collect 10 bags of tea
⦁	All the commands will be valid
⦁	All of the given numbers will be valid integers in the range [0, 10]
