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
