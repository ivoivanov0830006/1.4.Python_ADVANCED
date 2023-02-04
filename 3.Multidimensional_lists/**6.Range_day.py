matrix_size = 5
matrix = []
position = []
targets_left = []
targets_down = []

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
    if "x" in current_row:
        for target_index in range(len(current_row)):
            if current_row[target_index] == "x":
                targets_left.append([i, target_index])

number_commands = int(input())

for _ in range(number_commands):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == "move":
        steps = int(command[2])
        row = position[0] + directions[direction][0] * steps
        col = position[1] + directions[direction][1] * steps

        if 0 <= row < len(matrix) and 0 <= col < len(matrix):
            if matrix[row][col] == ".":
                matrix[position[0]][position[1]] = "."
                matrix[row][col] = "A"
                position = [row, col]
            elif matrix[row][col] == "x":
                position = [position[0], position[1]]
        else:
            position = [position[0], position[1]]

    elif action == "shoot":
        row, col = position[0] + directions[direction][0], position[1] + directions[direction][1]
        while 0 <= row < len(matrix) and 0 <= col < len(matrix):
            if matrix[row][col] == "x":
                matrix[row][col] = "."
                targets_left.remove([row, col])
                targets_down.append([row, col])
                break
            row, col = row + directions[direction][0], col + directions[direction][1]
        if not targets_left:
            break
if not targets_left:
    print(f"Training completed! All {len(targets_down)} targets hit.")
else:
    print(f"Training not completed! {len(targets_left)} targets left.")
print(*targets_down, sep="\n")


"""
------------------------------------ Problem to resolve --------------------------------

You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some 
symbols separated by a single space:
⦁	Your position is marked with the symbol "A"
⦁	Targets marked with symbol "x"
⦁	All of the empty positions will be marked with "."
After the field state, you will be given an integer representing the number of commands you will 
receive. The possible commands are:
⦁	"move {right/left/up/down} {steps}" – you should move in the given direction with the given 
steps. You can only move if the field you want to step on is marked with ".".
⦁	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current 
position without moving). Beware that there might be targets that stand in the way of other targets,
and you cannot reach them - you can shoot only the nearest target. When you have shot a target, the field becomes empty position (".").
Validate the positions since they can be outside the field.
Keep track of all the shot targets:
⦁	If at any point there are no targets left, end the program and print: 
        "Training completed! All {count_targets} targets hit.". 
⦁	If, after you perform all the commands, there are some targets left print: 
        "Training not completed! {count_left_targets} targets left.".
Finally, print the index positions of the targets that you hit, as shown in the examples.
Input
⦁	5 lines representing the field (symbols, separated by a single space)
⦁	N - count of commands
⦁	On the following N lines - the commands in the format described above
Output
⦁	On the first line, print one of the following:
⦁	If all the targets were shot
        "Training completed! All {count_targets} targets hit."
⦁	Otherwise:
        "Training not completed! {count_left_targets} targets left."
⦁	Finally, print the index positions 
        "[{row}, {column}]" of the targets that you hit, as shown in the examples.
Constrains
⦁	All the commands will be valid
⦁	There will always be at least one target
-------------------------------------- Example inputs ----------------------------------
Input
. . . . . 
x . . . . 
. A . . . 
. . . x . 
. x . . x 
3
shoot down
move right 4
move left 1	
Output
Training not completed! 3 targets left.
[4, 1]
----------------------------------------
Input
. . . . . 
. . . . . 
. A x . . 
. . . . . 
. x . . . 
2
shoot down
shoot right	
Output
Training completed! All 2 targets hit.
[4, 1]
[2, 2]
----------------------------------------
Input
. . . . . 
. . . . . 
. . x . . 
. . . . . 
. x . . A 
3
shoot down
move right 2
shoot left	
Output
Training not completed! 1 targets left.
[4, 1]

"""
