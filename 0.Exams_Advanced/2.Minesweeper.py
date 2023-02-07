def get_children(m, r, c):
    possible_children_coordinates = [
        [r - 1, c - 1],
        [r - 1, c],
        [r - 1, c + 1],
        [r, c - 1],
        [r, c + 1],
        [r + 1, c - 1],
        [r + 1, c],
        [r + 1, c + 1]
    ]

    result = []
    for child_r, child_c in possible_children_coordinates:
        if 0 <= child_r < len(m) and 0 <= child_c < len(m):
            result.append([child_r, child_c])
    return result


matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    current_row = []
    for _ in range(matrix_size):
        current_row.append(0)
    matrix.append(current_row)

mines_count = int(input())
position = []

for _ in range(mines_count):
    command = list(map(int, input().strip("(").strip(")").split(", ")))
    row, col = command[0], command[1]
    matrix[row][col] = "*"

    children = get_children(matrix, row, col)
    for child in children:
        child_row, child_col = int(child[0]), int(child[1])
        if matrix[child_row][child_col] != "*":
            matrix[child_row][child_col] += 1

for row in matrix:
    print(*row)

    
"""
------------------------------------ Problem to resolve --------------------------------

You will be given an integer n for the size of the mines field with square shape and another one 
for the number of bombs that you have to place in the field. On the next n lines, you will receive 
the position for each bomb. Your task is to create the game field placing the bombs at the correct 
positions and mark them with "*", and calculate the numbers in each cell of the field. Each cell represents 
a number of all bombs directly near it (up, down, left, right and the 4 diagonals).     
Input
⦁	On the first line, you are given the integer n – the size of the square matrix.
⦁	On the second line – the number of the bombs.
⦁	The next n lines holds the position of each bomb.
Output
⦁	Print the matrix you've created.
Constraints
⦁	The size of the square matrix will be between [2…15].
-------------------------------------- Example inputs ----------------------------------
Input	
4
4
(0, 3)
(1, 1)
(2, 2)
(3, 0)	
Output
1 1 2 *
1 * 3 2
2 3 * 1
* 2 1 1
----------------
Input
5
3
(1, 1)
(2, 4)
(4, 1)	
Output
1 1 1 0 0
1 * 1 1 1
1 1 1 1 *
1 1 1 1 1
1 * 1 0 0

"""
