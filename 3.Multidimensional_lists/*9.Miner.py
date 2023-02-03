matrix = []
matrix_size = int(input())
position = []
coals = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

input_directions = [x for x in input().split()]

for i in range(matrix_size):
    current_row = input().split()
    matrix.append(current_row)
    if "s" in current_row:
        position = [i, current_row.index("s")]
    if "e" in current_row:
        end_position = [i, current_row.index("e")]
    if "c" in current_row:
        for coal_index in range(len(current_row)):
            if current_row[coal_index] == "c":
                coals.append([i, coal_index])

game_over = False

for direction in input_directions:

    row, col = position[0] + directions[direction][0], position[1] + directions[direction][1]
    matrix[position[0]][position[1]] = "*"

    if 0 <= row < len(matrix) and 0 <= col < len(matrix):

        if matrix[row][col] == "*":
            matrix[row][col] = "s"
        elif matrix[row][col] == "c":
            matrix[row][col] = "s"
            coals.remove([row, col])
            if not coals:
                print(f"You collected all coal! ({row}, {col})")
                break
        elif matrix[row][col] == "e":
            print(f"Game over! ({row}, {col})")
            game_over = True
            break

        position = [row, col]

if coals and not game_over:
    print(f"{len(coals)} pieces of coal left. ({position[0]}, {position[1]})")


"""
------------------------------------ Problem to resolve --------------------------------

You are going to create a game called "Miner".
First, you will receive the size of a square field in which the miner should move. 
On the second line, you will receive the commands for the miner's movement, separated by a single space. 
The possible commands are "left", "right", "up" and "down". 
In the end, you will receive each row of the field on a separate line. The possible characters that may 
appear on the screen are:
⦁	* - a regular position on the field
⦁	e - the end of the route
⦁	c - coal
⦁	s - miner
The miner starts moving from the position "s". He should perform the given commands successively, moving 
with only one position in the given direction. If the miner has reached the edge of the field and the 
following command indicates that he has to get out of the area, he must remain in his current position and 
ignore the command.
When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. 
In the end, you should print whether the miner has succeeded in collecting the coal or not and his final 
position:
⦁	If the miner has collected all coal in the field, the program stops, and you should print the message: 
        "You collected all coal! ({row_index}, {col_index})".
⦁	If the miner steps at "e", the game is over (the program stops), and you should print the message: 
        "Game over! ({row_index}, {col_index})".
⦁	If there are no more commands and none of the above cases had happened, you should print the message: 
        "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
Input
⦁	Field size - an integer number
⦁	Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
⦁	The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
Output
⦁	There are three types of output as mentioned above.
Constraints
⦁	The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
⦁	The field will always have only one "s"
-------------------------------------- Example inputs ----------------------------------
Input	
5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *	
Output
Game over! (1, 3)
-------------------------------
Input
4
up right right right down
* * * e
* * c *
* s * c
* * * *	
Output
You collected all coal! (2, 3)
--------------------------------
Input
6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *	
Output
3 pieces of coal left. (5, 0)

"""
