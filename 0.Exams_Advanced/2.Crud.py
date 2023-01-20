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

    
"""
------------------------------------ Problem to resolve --------------------------------

In the beginning, you will be given a matrix with 6 rows and 6 columns - a table with information. 
It consists of:
    Letters - on one or many positions in the table
    Numbers - on one or many positions in the table
    Empty positions - marked with "."
Next, you will receive your first position on the table in the format:
            "({row}, {column})"
On the following lines, until you receive "Stop" you will be receiving commands in the format:
            "Create, {direction}, {value}"
The direction could be "up", "down", "left" or "right"
If you step in an empty position, create the given value on that position. E.g., 
if the given value is "A", and the position is empty (".") - change it to "A"
If the position is NOT empty, do NOT create a value on that position
            "Update, {direction}, {value}"
The direction could be "up", "down", "left" or "right"
If you step on a letter or number, update the position with the given value. E.g., 
if the given value is "h", and the position's value is "12" - change it to "h"
If the position is empty, do NOT update the value on that position
            "Delete, {direction}"
The direction could be "up", "down", "left" or "right"
If you step on a letter or number, delete it, and empty the position. E.g., 
if the given position's value is "h" - change it to "."
If the position is already empty, do NOT delete it
            "Read, {direction}"
The direction could be "up", "down", "left" or "right"
If you step on a letter or number, print it on the console
If the position is empty, do NOT read it
You can make only ONE move at a time in the given direction for each command given.
In the end, print the final matrix, each row on a new line, each position separated by a single space.
Constraints
You will always receive valid coordinates
You will always receive directions in the range of the table
You will always receive letters or numbers
-------------------------------------- Example inputs ----------------------------------
Input	
. . . . . .
. 6 . . . .
G . S . t S
. . 10 . . .
. 95 . . 8 .
. . P . . .
(1, 1)
Create, down, r
Update, right, e
Create, right, a
Read, right
Delete, right
Stop	
Output
t
. . . . . .
. 6 . . . .
G r e a t .
. . 10 . . .
. 95 . . 8 .
. . P . . .	
-----------------------
Input
. . . . . .  
. 6 . . . .  
. T . D . O  
. . 10 A . .  
. 95 . 80 5 .  
. . P . t .   
(2, 3)
Create, down, o
Delete, right
Read, up
Create, left, 20
Update, up, P
Stop	
Output
. . . . . .
. 6 . . . .
. T . D . O
. . 10 A . .
. 95 . 80 5 .
. . P . t .	
------------------------
Input
H 8 . . . .
70 i . . . .
t . . . B .
50 . 16 . C .
. . . t . .
. 25 . . . .
(0, 0)
Read, right
Read, down
Read, left
Delete, down
Create, right, 10
Read, left
Stop	
Output
8
i
70
H 8 . . . .
70 i . . . .
. 10 . . B .
50 . 16 . C .
. . . t . .
. 25 . . . .	

"""
