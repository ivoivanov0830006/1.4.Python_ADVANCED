size = int(input())

matrix = []
cruisers = []
start_position = []

for i in range(size):
    row = list(input())
    matrix.append(row)
    if "S" in row:
        start_position = [i, row.index("S")]
    if "C" in row:
        for c_index in range(len(row)):
            if row[c_index] == "C":
                cruisers.append([i, c_index])

hits = 0
destroyed = False
win = False
row, col = "", ""

while True:
    if hits > 2:
        destroyed = True
        break
    if not cruisers:
        win = True
        break

    command = input()
    next_position = []
    if command == "up":
        next_position = [start_position[0] - 1, start_position[1]]
    elif command == "down":
        next_position = [start_position[0] + 1, start_position[1]]
    elif command == "left":
        next_position = [start_position[0], start_position[1] - 1]
    elif command == "right":
        next_position = [start_position[0], start_position[1] + 1]

    row, col = next_position[0], next_position[1]
    matrix[start_position[0]][start_position[1]] = "-"   # matrix[row][col]

    if matrix[row][col] == "*":
        matrix[row][col] = "S"
        hits += 1

    elif matrix[row][col] == "C":
        matrix[row][col] = "S"
        position = [row, col]
        cruisers.pop(cruisers.index(position))

    matrix[row][col] = "S"
    start_position = next_position

if destroyed:
    print(f'Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!')
if win:
    print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
for row in matrix:
    print("".join(row))
