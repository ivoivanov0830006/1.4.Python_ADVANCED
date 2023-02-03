def is_outside(current_r, current_c, r, c):
    return current_r < 0 or current_c < 0 or current_r >= r or current_c >= c


def get_children(current_r, current_c, r, c):
    result = []
    possible_children_coordinates = [
        [current_r - 1, current_c],
        [current_r, current_c - 1],
        [current_r, current_c + 1],
        [current_r + 1, current_c]
    ]
    for current_child_row, current_child_col in possible_children_coordinates:
        if not is_outside(current_child_row, current_child_col, r, c):
            result.append([current_child_row, current_child_col])
    return result


input_rows, input_cols = [int(x) for x in input().split()]

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}

bunnies = set()
position = []
matrix = []

for i in range(input_rows):
    current_row = list(input())
    matrix.append(current_row)
    if "P" in current_row:
        position = [i, current_row.index("P")]
    if "B" in current_row:
        for bunny_index in range(len(current_row)):
            if current_row[bunny_index] == "B":
                bunnies.add(f"{i} {bunny_index}")

input_directions = input()

won = False
dead = False

for direction in input_directions:
    row, col = position[0] + directions[direction][0], position[1] + directions[direction][1]   # next pos
    matrix[position[0]][position[1]] = "."  # current pos

    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]
        children = get_children(bunny_row, bunny_col, input_rows, input_cols)
        for child_row, child_col in children:
            new_bunnies.add(f"{child_row} {child_col}")
            matrix[child_row][child_col] = "B"
            if child_row == row and child_col == col:
                dead = True
                break

    bunnies = bunnies.union(new_bunnies)

    if is_outside(row, col, input_rows, input_cols):
        position = [position[0], position[1]]
        won = True
        break
    elif matrix[row][col] == "B":
        position = [row, col]
        dead = True
        break
    else:
        matrix[row][col] = "P"
        position = [row, col]

for row in matrix:
    print("".join(row))
if won:
    print(f"won: {position[0]} {position[1]}")
if dead:
    print(f"dead: {position[0]} {position[1]}")


"""
------------------------------------ Problem to resolve --------------------------------

First, you will receive a line holding integers N and M, representing the lair's rows and columns.
Next, you receive N strings that can consist only of ".", "B", "P". They represent the initial state 
of the lair. There will be only one player. The bunnies are marked with "B", the player is marked with "P", 
and everything else is free space, marked with a dot ".". 
Then you will receive a string with commands (e.g., LRRULUD) - each letter represents the next move of 
the player:
⦁	L - the player should move one position to the left
⦁	R - the player should move one position to the right
⦁	U - the player should move one position up
⦁	D - the player should move one position down
After every step made, each bunny spreads one position up, down, left, and right. If the player moves to 
a bunny cell or a bunny reaches the player, the player dies. If the player goes out of the lair without 
encountering a bunny, the player wins.
When the player dies or wins, the game ends. All the activities for this turn continue (e.g., all the 
bunnies spread normally), but there are no more turns. There will be no cases where the moves of the 
player end before he dies or escapes.
In the end, print the final state of the lair with every row on a separate line. On the last line, print 
either "dead: {row} {col}" or "won: {row} {col}". "Row" and "col" are the cell coordinates where the player
has died or the last cell he has been in before escaping the lair.
Input
⦁	On the first line of input, the numbers N and M are received - the number of rows and columns in the lair
⦁	On the following N lines, each row is received in the form of a string. The string will contain 
    only ".", "B", "P". All strings will be the same length. There will be only one "P" for all the input
⦁	On the last line, the directions are received in the form of a string, containing "R", "L", "U", "D"
Output
⦁	On the first N lines, print the final state of the bunny lair
⦁	On the last line, print:
⦁	If the player won - "won: {row} {col}"
⦁	If the player dies - "dead: {row} {col}"
Constraints
⦁	The dimensions of the lair are in the range [3…20]
⦁	The directions string length is in the range [1…20]
-------------------------------------- Example inputs ----------------------------------
Input			
5 6
.....P
......
...B..
......
......
ULDDDR	
Output
......
...B..
..BBB.
...B..
......
won: 0 5
------------------
Input
4 5
.....
.....
.B...
...P.
LLLLLLLL	
Output
.B...
BBB..
BBBB.
BBB..
dead: 3 1
------------------
Input
5 8
.......B
...B....
....B..B
........
..P.....
ULLL
Output
BBBBBBBB
BBBBBBBB
BBBBBBBB
.BBBBBBB
..BBBBBB
won: 3 0

"""
