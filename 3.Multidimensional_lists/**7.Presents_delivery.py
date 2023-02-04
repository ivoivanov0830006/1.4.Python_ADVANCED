def cookie_func(current_directions, current_position):
    global presents_count
    for current_direction in current_directions.values():
        r, c = current_position[0] + current_direction[0], current_position[1] + current_direction[1]
        if matrix[r][c] == "X":
            presents_count -= 1
        if matrix[r][c] == "V":
            presents_count -= 1
            nice_kids_without_presents.remove([r, c])
            nice_kids_with_presents.append([r, c])
        matrix[r][c] = "-"
        if presents_count == 0:
            break
    return nice_kids_without_presents, nice_kids_with_presents


presents_count = int(input())
matrix_size = int(input())
matrix = []
position = []

nice_kids_without_presents = []
nice_kids_with_presents = []

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

for i in range(matrix_size):
    current_row = input().split()
    matrix.append(current_row)
    if "S" in current_row:
        position = [i, current_row.index("S")]
    if "V" in current_row:
        for target_index in range(len(current_row)):
            if current_row[target_index] == "V":
                nice_kids_without_presents.append([i, target_index])

while True:
    direction = input()
    if direction == "Christmas morning":
        break
    row, col = position[0] + directions[direction][0], position[1] + directions[direction][1]
    matrix[position[0]][position[1]] = "-"

    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if matrix[row][col] == "V":
            presents_count -= 1
            matrix[row][col] = "S"
            nice_kids_without_presents.remove([row, col])
            nice_kids_with_presents.append([row, col])
        if matrix[row][col] == "-":
            matrix[row][col] = "S"
        if matrix[row][col] == "X":
            matrix[row][col] = "S"
        if matrix[row][col] == "C":
            matrix[row][col] = "S"
            position = [row, col]
            cookie_func(directions, position)
            row, col = position[0], position[1]
        position = [row, col]
        if presents_count == 0 or len(nice_kids_without_presents) == 0:
            break

if presents_count == 0 and len(nice_kids_without_presents) > 0:
    print("Santa ran out of presents!")
for rows in matrix:
    print(*rows)
if nice_kids_without_presents:
    print(f"No presents for {len(nice_kids_without_presents)} nice kid/s.")
else:
    print(f"Good job, Santa! {len(nice_kids_with_presents)} happy nice kid/s.")


"""
------------------------------------ Problem to resolve --------------------------------

You will receive an integer m for the number of presents Santa has and an integer n for the size of the 
neighborhood with a square shape. On the following lines, you will receive the matrix, which represents 
the neighborhood. 
Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children 
may live. If the cell has "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives 
there, the cell is marked by "V". There can also be cells marked with "C" for cookies. All of the empty 
positions will be marked with "-".
Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that 
you receive. If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a 
house with a naughty kid, he doesn't drop a present. If the command sends Santa to a cell marked with "C", 
Santa eats cookies and becomes happy and extra generous to all the kids around him* (meaning all of them 
will receive presents - it doesn't matter if naughty or nice). If Santa has been to a house, the cell 
becomes "-".
Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa 
doesn't move to these cells, or if he does, he returns to the cell where the cookie was.
If Santa runs out of presents or receives the command "Christmas morning", you should end the program. 
Keep in mind that you should check whether all the nice kids received presents.
Input
⦁	On the first line, you are given the integer m - the count of presents
⦁	On the second - integer n - the size of the neighborhood
⦁	The following n lines hold the values for every row
⦁	On each of the following lines you will get a command
Output
⦁	On the first line:
⦁	If Santa runs out of presents, but there are still some nice kids left print: 
            "Santa ran out of presents!"
⦁	Next, print the matrix.
⦁	In the end, print one of these messages:
⦁	If he manages to give all the nice kids presents, print:
            "Good job, Santa! {count_nice_kids} happy nice kid/s."
⦁	Otherwise, print: 
            "No presents for {count nice kids} nice kid/s."
Constraints
⦁	The size of the square matrix will be between [2…10].
⦁	Santa's position will be marked with 'S'.
⦁	There will always be at least 1 nice kid.
⦁	There won't be a case where the cookie is on the border of the matrix.
