size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
coordinates = ((int(x) for x in coordinate.split(",")) for coordinate in input().split())

directions = (
    (-1, 0),        # up
    (1, 0),         # down
    (0, 1),         # right
    (0, -1),        # left
    (-1, 1),        # up-right
    (-1, -1),       # up-left
    (1, -1),        # down-left
    (1, 1),         # down-right
    (0, 0)          # current
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y
        if 0 <= r < size and 0 <= c < size:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

alive_cells_count = 0
alive_cells_sum = 0

for row in matrix:
    for element in row:
        if element > 0:
            alive_cells_count += 1
            alive_cells_sum += element

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")
for row in matrix:
    print(*row, sep=" ")
    
    
"""
------------------------------------- Another Solution ---------------------------------

def get_children(matrix, current_row, col):
    # possible child
    possible_children_coordinates = [
        [current_row - 1, col - 1],
        [current_row - 1, col],
        [current_row - 1, col + 1],
        [current_row, col - 1],
        [current_row, col + 1],
        [current_row + 1, col - 1],
        [current_row + 1, col],
        [current_row + 1, col + 1]
    ]

    result = []
    # filter about which one is true child
    for child_row, child_col in possible_children_coordinates:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])
    return result


size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

bombs = input().split()

for bomb in bombs:
    current_row, col = [int(x) for x in bomb.split(",")]
    power = matrix[current_row][col]

    if power <= 0:
        continue

    matrix[current_row][col] = 0

    children = get_children(matrix, current_row, col)
    for child_row, child_col in children:
        matrix[child_row][child_col] -= power

alive_cells_count = 0
alive_cells_sum = 0

for current_row in matrix:
    for element in current_row:
        if element > 0:
            alive_cells_count += 1
            alive_cells_sum += element

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")
for current_row in matrix:
    print(*current_row, sep=" ")
    
    
------------------------------------ Problem to resolve --------------------------------

You will be given a square matrix of integers, each integer separated by a single space, and each current_row will 
be on a new line. On the last line of input, you will receive indexes - coordinates of several cells separated
by a single space, in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
On those cells, there are bombs. You must detonate every bomb in the order they were given. When a bomb 
explodes, it deals damage equal to its integer value to all the cells around it (in every direction and in
all diagonals). One bomb can't explode more than once, and after it does, its value becomes 0. When a cell's
value reaches 0 or below, it dies. Dead cells can't explode.
You must print the count of all alive cells and their sum. Afterward, print the matrix with all its cells (including the dead ones).
Input
⦁	On the first line, you are given the integer N - the size of the square matrix.
⦁	The following N lines hold each column's values - N numbers separated by a space.
⦁	On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
Output
⦁	On the first line, you need to print the count of all alive cells in the format: 
"Alive cells: {alive_cells}"
⦁	On the second line, you need to print the sum of all alive cells in the format: 

⦁	In the end, print the matrix. A space must separate the cells.
Constraints
⦁	The size of the matrix will be between [0…1000].
⦁	The bomb coordinates will always be in the matrix.
⦁	The bomb's values will always be greater than 0.
⦁	The integers of the matrix will be in the range [1…10000]. 
